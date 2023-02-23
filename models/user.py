#!/usr/bin/python3
"""Create User Class"""
from models.base_model import BaseModel


class User (BaseModel):
    """User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""