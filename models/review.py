#!/usr/bin/python3
"""Create Review Class"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Review Class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        '''
        super().__init__(*args, **kwargs)
