# Importing necessary modules from the model definition and marshmallow for serialization/deserialization
from .models import Location
from marshmallow import Schema, fields

class LocationSchema(Schema):
    """
    Schema definition for the Location model to support serialization and deserialization.
    Uses the Marshmallow library for data transformation and validation.
    """
    
    # Defining fields that map to the Location model properties
    id = fields.Integer(description="Unique identifier for the location.")
    person_id = fields.Integer(description="Identifier for the person associated with the location.")
    longitude = fields.String(attribute="longitude", description="Longitude coordinate of the location.")
    latitude = fields.String(attribute="latitude", description="Latitude coordinate of the location.")
    creation_time = fields.DateTime(description="Timestamp when the location data was created.")
    
    class Meta:
        """
        Meta class provides additional options and configurations.
        """
        
        model = Location  # Specifies the associated ORM model for this schema
