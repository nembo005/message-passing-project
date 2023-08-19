import os
from typing import List, Type

# Environment variables for database configuration with default values
DB_USERNAME = os.getenv("DB_USERNAME", "default_username")
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_password")
DB_HOST = os.getenv("DB_HOST", "default_host")
DB_PORT = os.getenv("DB_PORT", "default_port")
DB_NAME = "location_database"

class BaseConfig:
    """Base configuration class. Contains default settings."""
    
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Turns off notifications for database change events


class DevelopmentConfig(BaseConfig):
    """Development configuration. Inherits from BaseConfig and overrides some of its values."""
    
    CONFIG_NAME = "dev"
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"  # Default secret key for development
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    # Constructing database URL for PostgreSQL
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class TestingConfig(BaseConfig):
    """Testing configuration. Inherits from BaseConfig and overrides some of its values."""
    
    CONFIG_NAME = "test"
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")  # Default secret key for testing
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    # Constructing database URL for PostgreSQL
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class ProductionConfig(BaseConfig):
    """Production configuration. Inherits from BaseConfig and overrides some of its values."""
    
    CONFIG_NAME = "prod"
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "I'm Ron Burgundy?")  # Default secret key for production
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    # Constructing database URL for PostgreSQL
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

# List of configurations exported by this module
EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
# Dictionary mapping configuration names to their respective classes, facilitating dynamic selection
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
