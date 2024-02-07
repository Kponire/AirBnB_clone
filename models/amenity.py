#!/usr/bin/python3

"""Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
