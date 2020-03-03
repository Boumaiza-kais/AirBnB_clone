#!/usr/bin/python
""" Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review class"""
        super().__init__(*args, **kwargs)
