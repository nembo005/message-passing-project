# Importing necessary modules for logging, data manipulation, ORM, and other utility services.
import logging
from datetime import datetime, timedelta
from typing import Dict, List

from flask_sqlalchemy import SQLAlchemy
from .models import Location
from .schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from .kafkaservice import KafkaService

# Setting up the database session
db = SQLAlchemy()

# Configuring the logging for this module
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location-api")

class LocationService:
    """
    Provides services related to the Location model, such as retrieving and creating location data.
    """

    @staticmethod
    def retrieve(location_id) -> Location:
        """
        Fetches a specific location by its ID from the database.

        :param location_id: The unique identifier of the location.
        :return: Location instance matching the provided ID.
        """
        
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())  # Extracting location and its coordinates as text
            .filter(Location.id == location_id)
            .one()
        )

        # Set the text representation of the coordinate on the location object
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        """
        Creates a new location record in the database and sends a message to Kafka with its ID.

        :param location: Dictionary containing the data for the location to be created.
        :return: The created Location instance.
        """
        
        # Validate the input data against the Location schema
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        # Constructing the new Location object
        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        # Convert the latitude and longitude to a point representation in the database
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        
        # Adding the new location to the session and committing it to save in the database
        db.session.add(new_location)
        db.session.commit()

        # Send a message with the new location ID to the Kafka topic
        kafka_service = KafkaService(kafka_topic="location_topic")
        kafka_service.send_message(str(new_location.id))

        return new_location
