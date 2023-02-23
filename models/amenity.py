#!/usr/bin/python3
"""Create Amenity Class"""
from models.base_model import BaseModel


class Amenity (BaseModel):
    """Amenity Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        '''
        super().__init__(*args, **kwargs)
