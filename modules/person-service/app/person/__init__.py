# Importing the Person model.
# The `# noqa` comment is used to inform linters (like flake8) to ignore this line.
# This is typically done for imports that are used elsewhere (like in __init__.py) but not directly in this file.
from .models import Person  # noqa

# Importing the schema for the Person model.
from .schemas import PersonSchema  # noqa

def register_routes(api, app, root="api"):
    """
    This function is responsible for registering the routes associated with the 'Person' operations.

    Args:
    - api: The instance of the Flask-Restx API.
    - app: The Flask application instance.
    - root (str): The root path to which the API namespace will be added. Defaults to "api".

    Returns:
    None
    """

    # Locally importing the controllers for the 'Person' operations to avoid potential circular imports.
    from .controllers import api as person_api

    # Adding the namespace (from the person controllers) to the API under the provided root path.
    api.add_namespace(person_api, path=f"/{root}")
