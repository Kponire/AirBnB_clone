#!/usr/bin/python3

"""Dfine the class FileStorage."""
import json


class FileStorage:
    """introduce the class FileStorage.

    Description:
        serialize instance object to json file and,
        deserialize json file to instance object.
    """
    __file_path = "file.json"   # path to the JSON file
    __objects = dict()

    def all(self):
        """Returns a dictionary '__object'."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file."""
        with open(self.__file_path, "w") as obj_file:
            json.dump(self.__objects, obj_file)

    def reload(self):
        """deserializes the JSON file to __objects.

        Return:
            returns the instance object.
        """
        if self.__file_path:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
            return self.__objects
        else:
            return None
