from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db_instance = SQLAlchemy()

def initialize_app(environment=None):
    """
    Initialize the Flask application, configure it, and set up routes.

    Parameters:
        environment (str, optional): The environment for the configuration (e.g., "test", "prod"). 
                                     Defaults to "test" if not provided.

    Returns:
        Flask: Initialized Flask application instance.
    """

    # Importing local modules necessary for setting up the app
    from .config import config_selector
    from .routes import bind_routes

    # Create a Flask application instance
    application = Flask(__name__)

    # Load the appropriate configuration based on the provided environment
    application.config.from_object(config_selector[environment or "test"])

    # Initialize the Flask-RestX API with the app
    api_instance = Api(application, title="Connection Service API", version="0.1.0")
    
    # Initialize Flasgger for Swagger UI generation
    Swagger(application)

    # Enable CORS, useful for development purposes when making requests from a different domain
    CORS(application)

    # Bind the defined routes to the API instance
    bind_routes(api_instance, application)

    # Bind the application with the SQLAlchemy instance
    db_instance.init_app(application)

    @application.route("/health")
    def check_health():
        """
        Endpoint for health checks. Useful for monitoring and orchestration.

        Returns:
            JSONResponse: Indicates that the service is operational.
        """
        return jsonify("operational")

    return application
