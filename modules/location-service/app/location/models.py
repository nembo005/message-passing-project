# Importing necessary libraries for data modeling and type annotations
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from app import db  # Importing the database instance
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry.point import Point
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property

class Location(db.Model):
    """
    Database model for storing geolocation data.
    """
    
    # Defining the table name in the database
    __tablename__ = "location"

    # Defining columns and data types
    id = Column(BigInteger, primary_key=True)
    person_id = Column(Integer, nullable=False)
    coordinate = Column(Geometry("POINT"), nullable=False)
    creation_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    _wkt_shape: str = None  # Temporary storage for the Well-Known Text (WKT) representation of the point

    @property
    def wkt_shape(self) -> str:
        """
        Convert binary geometry representation to Well-Known Text (WKT) format.
        """
        if not self._wkt_shape:
            point: Point = to_shape(self.coordinate)
            # Normalize the WKT string format to match the database representation
            self._wkt_shape = point.to_wkt().replace("POINT ", "ST_POINT")
        return self._wkt_shape

    @wkt_shape.setter
    def wkt_shape(self, v: str) -> None:
        """
        Set the _wkt_shape value.
        
        :param v: The WKT string value to set.
        """
        self._wkt_shape = v

    def set_wkt_with_coords(self, lat: str, long: str) -> str:
        """
        Set the WKT representation using provided latitude and longitude.
        
        :param lat: Latitude value.
        :param long: Longitude value.
        :return: The updated WKT representation.
        """
        self._wkt_shape = f"ST_POINT({lat} {long})"
        return self._wkt_shape

    @hybrid_property
    def longitude(self) -> str:
        """
        Extract the longitude from the WKT representation.
        
        :return: Longitude value.
        """
        coord_text = self.wkt_shape
        return coord_text[coord_text.find(" ") + 1 : coord_text.find(")")]

    @hybrid_property
    def latitude(self) -> str:
        """
        Extract the latitude from the WKT representation.
        
        :return: Latitude value.
        """
        coord_text = self.wkt_shape
        return coord_text[coord_text.find("(") + 1 : coord_text.find(" ")]

@dataclass
class Connection:
    """
    Data class for managing connections, which is associated with a location.
    """
    
    location: Location
