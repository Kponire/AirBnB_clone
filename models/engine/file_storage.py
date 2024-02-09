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

    def all(self, cls=None):
        """Returns a dictionary '__object'."""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        if obj is not None:
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

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def count(self, cls=None):
        """returns the number of objects in storage matching the given class.
        If no class is passed, returns the count of all objects in storage."""
        if cls is None:
            return len(models.storage.all())
        return len(models.storage.all(cls))

    def get(self, cls, id):
        """returns the object based on the class and its ID,
        or None if not found"""
        if cls is None:
            return None
        if type(cls) is str:
            if cls not in classes:
                return None
            cls = classes[cls]
        save = models.storage.all(cls)
        return save.get("{}.{}".format(cls.__name__, id))
