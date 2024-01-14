#!/usr/bin/python3
"""
This module contains the base class
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    The Base Class
    """
    def __init__(self, *args, **kwargs):
        """
        Public instantiation for Instance of class
        """
        date_time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_time))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        Save to storage and update current time
        """
        self.updated_at = datetime.utcnow()

        models.storage.save()

    def to_dict(self):
        """
        Return the dict representation of object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns String representation of objects
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
