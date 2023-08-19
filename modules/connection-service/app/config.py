import os
from typing import List, Type

# Environment variables to configure the database connection.
# If not found in the environment, defaults are provided.
DB_USER = os.getenv("DB_USER", "default_user")
DB_PASS = os.getenv("DB_PASS", "default_pass")
DB_ENDPOINT = os.getenv("DB_ENDPOINT", "default_endpoint")
DB_SERVICE_PORT = os.getenv("DB_SERVICE_PORT", "default_service_port")
DATABASE_NAME = "connection_database"


class ConfigBase:
    """
    Base configuration class. Contains common configuration settings across all environments.
    """
    NAME = "base"
    USE_MOCK_DATA = False
    IS_DEBUG = False
    TRACK_SQLALCHEMY = False  # For performance, track_modifications is set to False.


class ConfigDevelopment(ConfigBase):
    """
    Development environment configuration.
    """
    NAME = "development"
    SECRET = os.getenv(
        "DEV_SECRET", "Marlon Brando's Eyes couldn't see California"
    )
    IS_DEBUG = True
    TRACK_SQLALCHEMY = False
    IS_TESTING = False
    SQLALCHEMY_DB_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}:{DB_SERVICE_PORT}/{DATABASE_NAME}"
    )


class ConfigTesting(ConfigBase):
    """
    Testing environment configuration.
    """
    NAME = "testing"
    SECRET = os.getenv("TEST_SECRET", "The snap by Thanos was justified")
    IS_DEBUG = True
    TRACK_SQLALCHEMY = False
    IS_TESTING = True
    SQLALCHEMY_DB_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}:{DB_SERVICE_PORT}/{DATABASE_NAME}"
    )


class ConfigProduction(ConfigBase):
    """
    Production environment configuration.
    """
    NAME = "production"
    SECRET = os.getenv("PRODUCTION_SECRET", "Stay classy, San Diego")
    IS_DEBUG = False
    TRACK_SQLALCHEMY = False
    IS_TESTING = False
    SQLALCHEMY_DB_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}:{DB_SERVICE_PORT}/{DATABASE_NAME}"
    )

def config_selector(environment_name: str) -> Type[ConfigBase]:
    return config_by_key.get(environment_name, ConfigBase)

# Exported configurations, making them accessible as a list for easy lookup and iteration.
EXPORTED_CONFIGS: List[Type[ConfigBase]] = [
    ConfigDevelopment,
    ConfigTesting,
    ConfigProduction,
]

# Dictionary to access configuration classes by their NAME attribute.
config_by_key = {config.NAME: config for config in EXPORTED_CONFIGS}
