from flask import Blueprint
from .connection.controllers import api_description

def initialize_routes(application):
    """
    Initializes routes by creating a Blueprint and associating it with the given Flask application.
    
    Parameters:
    - application: The Flask application instance to which the routes should be registered.
    """
    # Creating a Blueprint instance for routing.
    blueprint_instance = Blueprint('api', __name__, url_prefix='/api')
    
    # Initializing the api_description with the blueprint.
    api_description.init_app(blueprint_instance)
    
    # Registering the blueprint with the Flask application.
    application.register_blueprint(blueprint_instance)

def bind_routes(api_instance, application, base="api"):
    """
    Binds specific routes from the 'connection' module to the application.

    Parameters:
    - api_instance: The Flask-Restx API instance which provides Swagger UI and other functionalities.
    - application: The Flask application instance to which the routes should be registered.
    - base (optional): A prefix for the routes, defaults to "api".
    """
    from .connection.controllers import bind_routes as connect_routes

    # Invoking the binding function from the 'connection' module to register its routes.
    connect_routes(api_instance, application)
