#!/usr/bin/python3
"""Create FileStorage Class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage Class"""

    __file_path: str = "file.json"
    __objects: object = {}

    def __init__(self) -> None:
        pass

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj) -> None:
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if not obj:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        data_dict = {}
        classes = {
            "BaseModel": BaseModel,
        }
        try:
            with open(self.__file_path, 'r') as file:
                data_dict = json.load(file)
                for key, value in data_dict.items():
                    self.__objects[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
