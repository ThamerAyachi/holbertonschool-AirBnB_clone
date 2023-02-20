#!/usr/bin/python3
"""Create Base Class"""
import uuid
import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self) -> None:
        """Update 'update_at' to current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Make class to dictionary"""
        attributes = self.__dict__.copy()
        attributes["__class__"] = self.__class__.__name__
        attributes["created_at"] = self.created_at.isoformat()
        attributes["updated_at"] = self.updated_at.isoformat()
        return attributes
