#!/usr/bin/python3

"""City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Representation of  City.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
