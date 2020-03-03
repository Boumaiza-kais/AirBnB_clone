#!/usr/bin/python
""" State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state class"""
        super().__init__(*args, **kwargs)
