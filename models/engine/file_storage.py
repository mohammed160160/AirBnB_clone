#!/usr/bin/python3
"""
Modeule for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class that serializes instances to a Json file, \
    and deserializes Json file to Instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets an object in the __objects dictionary using
        <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects dictionary into
        JSON format and saves it to the file specified by __file_path.
        """
        obj_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        obj = eval(class_name)(**value)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass
