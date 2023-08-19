from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Initializing the database instance
db = SQLAlchemy()

def create_app(env=None):
    """
    Creates and configures the Flask application.
    
    :param env: The environment for which the configuration should be loaded.
    :return: Configured Flask application instance.
    """
    from .config import config_by_name
    from .routes import register_routes

    # Create Flask app and load configuration settings
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    
    # Initialize API with the Flask app
    api = Api(app, title="Connection Microservice API", version="0.1.0")

    # Configuration settings for Flasgger (Swagger UI)
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
    # Initialize Flasgger with the Flask app and the provided configuration
    swagger = Swagger(app, config=swagger_config)

    # Enable CORS for the Flask app
    CORS(app)  

    # Register the routes for the Flask app
    register_routes(api, app)
    
    # Initialize the database with the Flask app
    db.init_app(app)

    @app.route("/health")
    def health():
        """ 
        Endpoint to check the health status of the application.
        
        :return: A JSON response indicating that the application is healthy.
        """
        return jsonify("healthy")

    return app
