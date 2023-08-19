from datetime import datetime
from flasgger import swag_from
from marshmallow import Schema, fields as ma_fields
from .models import ConnectionData
from .schemas import ConnectionDataSchema
from .services import ConnectionDataManager
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, Api, fields

from .kafkaservice import KafkaUtility

# Initialize Kafka Service instance with topic name
kafka_instance = KafkaUtility(kafka_topic_name="kafka_topic_name")

# Format for date handling
DATE_FMT = "%Y-%m-%d"

# Namespace instance for organizing endpoints and documentation
api_description = Namespace("UdaConnect", description="Geolocation-based Connections.")

# API instance with a version number, title, and description
api_instance = Api(version='1.0', title='Connection API Interface', description='Connection API Description',)

# Grouping API endpoints under a common namespace
ns = api_description.namespace('connections', description='Manage connections')

# Connection data model, which defines the expected fields and their properties
conn_model = api_instance.model('ConnectionDetail', {
    'id': fields.String(required=True, description='Unique connection ID'),
    'name': fields.String(required=True, description='Connection metadata'),
})

# Schema for basic response messages
class ResponseSchema(Schema):
    message = ma_fields.Str(required=True)

# Endpoint for listing and creating connections
@ns.route('/')
class ListConnections(Resource):
    @swag_from('modules/connection-service/swagger_specs/list_connections.yaml')
    @ns.doc('retrieve_connections')
    def get(self):
        pass

    @swag_from('modules/connection-service/swagger_specs/create_connection.yaml')
    @ns.doc('add_connection')
    @ns.expect(conn_model)
    def post(self):
        pass

# Endpoint for checking the API status
@api_instance.route("/api/")
class APIStatusResource(Resource):
    @responds(schema=ResponseSchema)
    def get(self) -> dict:
        return {"message": "API functioning properly"}, 200

# Endpoint for fetching connection data related to a specific person, based on query parameters
@api_instance.route("/persons/<person_id>/connection")
@api_instance.param("start_date", "Start Date Range", _in="query")
@api_instance.param("end_date", "End Date Range", _in="query")
@api_instance.param("distance", "User proximity in meters", _in="query")
class ConnectionDataHandler(Resource):
    @responds(schema=ConnectionDataSchema, many=True)
    def get(self, person_id) -> ConnectionDataSchema:
        pass

# Function to bind the API instance to a specific base URL and add it to the Flask application
def bind_routes(api_instance, application, base="api"):
    api_instance.add_namespace(api_instance)
