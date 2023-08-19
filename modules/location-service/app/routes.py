from flask import Blueprint
from .location.controllers import api

def configure_routes(app):
    """
    Configures and initializes the API routes for the application.

    Args:
        app (Flask): The Flask application instance.

    """
    blueprint = Blueprint('api', __name__, url_prefix='/api')  # Define a new Blueprint for API routes with the prefix '/api'
    api.init_app(blueprint)  # Initialize the API with the defined blueprint
    app.register_blueprint(blueprint)  # Register the blueprint with the Flask application instance

def register_routes(api, app, root="api"):
    """
    Registers the application routes.

    Args:
        api (Api): The Flask-RESTx API instance.
        app (Flask): The Flask application instance.
        root (str, optional): The root namespace for the API. Defaults to "api".

    """
    from .location.controllers import register_routes as attach_location

    # Attach the location-related routes to the API
    attach_location(api, app)
