#!/usr/bin/python3
"""Create State Class"""
from models.base_model import BaseModel


class State (BaseModel):
    """State Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        '''
        super().__init__(*args, **kwargs)
