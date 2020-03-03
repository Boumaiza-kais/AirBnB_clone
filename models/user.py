#!/usr/bin/python
""" user class """
from models.base_model import BaseModel


class User(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user class"""
        super().__init__(*args, **kwargs)
