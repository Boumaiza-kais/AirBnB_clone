#!/usr/bin/python3
""" FileStorage class """

import uuid
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all """
        return FileStorage.__objects

    def new(self, obj):
        """ add new object """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        new_dict = {}

        for keys in FileStorage.__objects.keys():
            new_dict[keys] = (FileStorage.__objects[keys]).to_json()

        with open(self.__file_path, mode="w") as f:
            json.dump(new_dict, f)


    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
