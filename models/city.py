#!/usr/bin/python3
"""Create City Class"""
from models.base_model import BaseModel


class City (BaseModel):
    """City Class"""

    state_id: str = ""
    name: str = ""
    
    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        '''
        super().__init__(*args, **kwargs)
