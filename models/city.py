#!/usr/bin/python
""" class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
