from dataclasses import dataclass
from typing import Dict

@dataclass
class ConnectionData:
    """
    A data class representing a connection between a geographical location and an individual.

    Attributes:
        geo_location (Dict): Data related to the geographical location. It represents 
                             the location data in the form of a dictionary.
        individual (Dict): Data related to the individual. It represents the person's
                           details in the form of a dictionary.
    """

    geo_location: Dict  # Geographic location data
    individual: Dict    # Individual's personal data
