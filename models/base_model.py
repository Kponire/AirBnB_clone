#!/usr/bin/python3

"""Define a class baseModel."""

from datetime import datetime
import models
import uuid


class BaseModel:
    """Introduces the class BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize the class BaseModel

        Args:
            args: variable positional argument passed to the class
            kwargs: variable keyword argument passed to the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        obj_time = datetime.strptime(
                            value,
                            "%Y-%m-%dT%H:%M:%S.%f"
                        )
                        setattr(self, key, obj_time)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """string representation of the the class BaseModel."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the public instance with current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''convert time object into string.

        Return:
            Returns a dictionary contaning all keys and valus
        '''
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
