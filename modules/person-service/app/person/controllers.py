# Importing necessary modules and libraries
from flask import request
from flasgger import swag_from
from flask_restx import Namespace, Resource
from .models import Person
from .services import PersonService
from .schemas import PersonSchema
from marshmallow import Schema, fields
from flask_accepts import responds

# Setting up the namespace for person operations
api = Namespace("UdaConnect", description="Operations related to managing persons.") 

# Defining a schema to standardize response messages
class MessageSchema(Schema):
    message = fields.Str(required=True)

# Route for getting API status
@api.route("/api/")
class APIInfoResource(Resource):
    @responds(schema=MessageSchema)
    def get(self) -> dict:
        """
        Checks and confirms if the API is operational.

        Returns:
        dict: A dictionary containing a status message.
        """
        return {"message": "API is operational"}, 200

# Route for performing operations on persons
@api.route("/persons")
class PersonResource(Resource):
    @swag_from('modules/person-service/swagger_specs/list_persons.yaml')  
    def get(self):
        '''Retrieve a list of all persons'''
        persons = PersonService.retrieve_all()
        return PersonSchema().dump(persons, many=True)

    @swag_from('modules/person-service/swagger_specs/create_person.yaml')  
    def post(self):
        '''Add a new person to the system'''
        new_person_data = request.get_json()
        new_person = PersonService.create(new_person_data)
        return PersonSchema().dump(new_person)

# Route for fetching a person by its ID
@api.route("/persons/<person_id>")
class PersonResourceById(Resource):
    @swag_from('modules/person-service/swagger_specs/get_person.yaml')  
    def get(self, person_id):
        '''Fetch a person based on the provided ID'''
        person = PersonService.retrieve_by_id(person_id)
        return PersonSchema().dump(person)

# Function to register the above routes and namespaces
def register_routes(api, app, root="api"):
    """
    Register the routes to the provided API instance under the given root.

    Args:
    - api: Instance of the Flask-Restx API.
    - app: Flask application instance.
    - root (str): Base path for the API routes. Defaults to "api".

    Returns:
    None
    """
    api.add_namespace(api)
