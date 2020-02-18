#!/usr/bin/python3
""" Module for Base """

from datetime import datetime
from uuid import uuid4
import models

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Basemodel class """
    def __init__(self, *args, **kwargs):
        """ Initialization of Database """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, format_dt)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, format_dt)
                elif key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """ to_dict containing all keys/values of the instance """
        dic = self.__dict__.copy()
        dic.update({"__class__": __class__.__name__})
        dic.update({"created_at": self.created_at.isoformat()})
        dic.update({"updated_at": self.updated_at.isoformat()})
        return dic

    def __str__(self):
        """ str Generate a string object """
        return("[{}] ({}) {}".format(name_c, self.id, self.__dict__))

    def save(self):
        """ Public instance to updated with the current datetime """
        self.updated_at = datetime.now()
        storage.save()
