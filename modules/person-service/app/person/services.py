import logging
from typing import Dict, List

from flask_sqlalchemy import SQLAlchemy
from .models import Person
from .schemas import PersonSchema

# Initializing the database instance
db = SQLAlchemy()

# Setting up logging configurations
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("person-api")

# Service class to handle operations related to `Person`
class PersonService:
    
    @staticmethod
    def create(person: Dict) -> Person:
        """
        Creates a new `Person` record in the database using provided data.

        :param person: Dictionary containing details for a new person.
        :return: The created `Person` object.
        """
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        # Add the new person to the session and commit changes to the database
        db.session.add(new_person)
        db.session.commit()

        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        """
        Retrieves a `Person` record from the database using the provided ID.

        :param person_id: The ID of the person to retrieve.
        :return: The `Person` object with the provided ID or None if not found.
        """
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        """
        Retrieves all `Person` records from the database.

        :return: List of all `Person` objects in the database.
        """
        return db.session.query(Person).all()
