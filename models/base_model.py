#!/usr/bin/python3
"""Create Base Class"""
import uuid
import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.create_at = datetime.datetime.now()
        self.update_at = self.create_at

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self) -> None:
        """Update 'update_at' to current time"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """Make class to dictionary"""
        attributes = self.__dict__.copy()
        attributes["__class__"] = self.__class__.__name__
        attributes["create_at"] = self.create_at.isoformat()
        attributes["update_at"] = self.update_at.isoformat()
        return attributes
