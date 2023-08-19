# Standard library imports
from marshmallow import Schema, fields
from flask import request
from flask_restx import Namespace, Resource

# Third-party library imports
from flasgger import swag_from
from flask_accepts import accepts, responds

# Local module imports
from .models import Location
from .schemas import LocationSchema
from .services import LocationService
from .grpcservice import GRPCService

# Setting up a namespace for the UdaConnect endpoints
api = Namespace("UdaConnect", description="Connections via geolocation.")

# Schema definition for API message responses
class MessageSchema(Schema):
    """Defines the schema for messages returned by the API."""
    message = fields.Str(required=True)

# Endpoint to verify if the API is working
@api.route("/api/")
class APIInfoResource(Resource):
    """Endpoint to return API status."""

    @swag_from('modules/location-service/swagger_specs/api_info.yaml')
    @responds(schema=MessageSchema)
    def get(self) -> dict:
        """Returns a status message indicating the API's operational status."""
        return {"message": "API is working"}, 200

# Resource endpoints for location operations
@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    """Endpoint to handle operations related to Location entities."""

    @swag_from('modules/location-service/swagger_specs/create_location.yaml')
    @accepts(schema=LocationSchema)  # Validates the incoming request data.
    @responds(schema=LocationSchema) # Specifies the response schema.
    def post(self) -> Location:
        """Creates and returns a new Location using the input data."""
        location_data = request.get_json()
        location: Location = LocationService.create(location_data)
        
        # Uses the GRPC service to send location data.
        grpc_service = GRPCService(server_address="[::]:50051")
        grpc_response = grpc_service.send_location(location_data)
        
        return location

    @swag_from('modules/location-service/swagger_specs/get_location.yaml')
    @responds(schema=LocationSchema) # Specifies the response schema.
    def get(self, location_id) -> Location:
        """Retrieves and returns a Location by its ID."""
        location: Location = LocationService.retrieve(location_id)
        return location

# Function to register the routes with the app
def register_routes(api, app, root="api"):
    """Attaches the UdaConnect namespace to the main API."""
    api.add_namespace(api, path=f"/{root}")
