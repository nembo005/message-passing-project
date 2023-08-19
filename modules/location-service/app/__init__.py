# Importing core Flask modules and extensions for API, database, documentation, and CORS handling
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Global database instance
db = SQLAlchemy()

def create_app(env=None):
    """
    Creates and configures the Flask application.

    :param env: The environment for configuration. Defaults to 'test'.
    :return: Configured Flask app instance.
    """
    
    # Importing configuration mappings and route registration utility
    from .config import config_by_name
    from .routes import register_routes

    # Creating a Flask instance
    app = Flask(__name__)
    
    # Loading configuration based on the environment
    app.config.from_object(config_by_name[env or "test"])
    
    # Creating an API instance for our app
    api = Api(app, title="Connection Microservice API", version="0.1.0")

    # Flasgger configuration for Swagger UI and documentation generation
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/",
    }
    
    # Initializing Flasgger with the Flask app for Swagger-based documentation
    swagger = Swagger(app, config=swagger_config)

    # Enabling CORS for the app, particularly useful for development phase
    CORS(app)

    # Registering routes and initializing the database with the app
    register_routes(api, app)
    db.init_app(app)

    # Health check route to verify the application's health status
    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
