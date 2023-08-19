# Importing necessary features for type hinting and SQLAlchemy functionality
from __future__ import annotations

from sqlalchemy import Column, Integer, String
from app import db  

# Define the `Person` model which will map to the "person" table in the database
class Person(db.Model):
    __tablename__ = "person"  # Specifies the name of the table in the database

    # Columns for the table
    id = Column(Integer, primary_key=True, comment="Unique identifier for a person.")
    first_name = Column(String, nullable=False, comment="First name of the person.")
    last_name = Column(String, nullable=False, comment="Last name of the person.")
    company_name = Column(String, nullable=False, comment="Company name associated with the person.")
