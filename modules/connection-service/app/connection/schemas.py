from .models import ConnectionData
from marshmallow import Schema, fields

class ConnectionDataSchema(Schema):
    """
    Schema for ConnectionData model, which is used for serialization 
    and deserialization of ConnectionData objects.

    Attributes:
        geo_location_id (Integer): ID associated with a geographical location.
        individual_id (Integer): ID associated with an individual.
        timestamp (DateTime): Timestamp indicating when the connection was established or recorded.
    """

    geo_location_id = fields.Integer(description="ID of the geographical location.")
    individual_id = fields.Integer(description="ID of the individual.")
    timestamp = fields.DateTime(description="Timestamp of the connection data.")

    class Meta:
        """Metadata class for additional schema configurations."""
        model = ConnectionData  # The associated model for this schema
