#!/usr/bin/python3

"""State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Representation of State.

    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
