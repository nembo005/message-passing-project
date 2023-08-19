from flask import Blueprint
from .person.controllers import api

def configure_routes(app):
    """
    Initialize routes with the given application.

    Args:
        app: Flask application instance.

    Returns:
        None
    """
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

def register_routes(api, app, root="api"):
    """
    Register routes with the given API and application.

    Args:
        api: Flask-RESTx API instance.
        app: Flask application instance.
        root: The base URL for the API endpoints. Default is "api".

    Returns:
        None
    """
    from .person.controllers import register_routes as attach_person

    # Attach person-specific routes to the API.
    attach_person(api, app)
