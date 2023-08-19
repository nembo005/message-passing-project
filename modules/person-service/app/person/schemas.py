# Import necessary libraries for model and serialization
from .models import Person
from marshmallow import Schema, fields

# Define the `PersonSchema` for serializing/deserializing Person objects
class PersonSchema(Schema):
    # Fields that will be serialized/deserialized
    id = fields.Integer(description="Unique identifier for a person.")
    first_name = fields.String(description="First name of the person.")
    last_name = fields.String(description="Last name of the person.")
    company_name = fields.String(description="Company name associated with the person.")

    # Metadata class to associate the schema with the `Person` model
    class Meta:
        model = Person  # Reference to the Person model
