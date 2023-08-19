# Required component imports
from .models import Location  # noqa
from .schemas import LocationSchema  # noqa

# Function to register the routes with the app
def register_routes(api, app, root="api"):
    """Register routes for the UdaConnect namespace."""
    
    # Local import of the controllers module to avoid circular imports
    from .controllers import api as location_api

    # Attach the namespace to the main API
    api.add_namespace(location_api, path=f"/{root}")
