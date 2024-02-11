#!/usr/bin/python3
"""
    This module defines the BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, self.time_fmt))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        Updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method returns a dictionary containing all keys/values of
        ___dict__ instance of BaseModel class
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """
        Return string representation of BaseModel class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
