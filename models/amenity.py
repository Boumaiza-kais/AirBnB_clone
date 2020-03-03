#!/usr/bin/python
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity class"""
        super().__init__(*args, **kwargs)
