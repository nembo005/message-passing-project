# Import necessary models and schemas
from .models import ConnectionData
from .schemas import ConnectionDataSchema

def setup_routes(api_instance, application, base="api"):
    # Import the API namespace from the local 'controllers' module
    # This is done inside the function to avoid potential circular imports
    from .controllers import api as conn_api
    
    # Add the namespace to the provided API instance, under the specified base path
    api_instance.add_namespace(conn_api, path=f"/{base}")
