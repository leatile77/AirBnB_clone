#!/usr/bin/python3

from datetime import datetime
import json
import uuid
import models

class BaseModel:
    """Defines BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        Instantiates class.
        """
        frmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, frmt))
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def save(self):
        """
        Update the updated_at attribute and save to storage
        """
        
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Converts object attributes to dictionary format
        """
        dict_instance = self.__dict__.copy()
        dict_instance["__class__"] = self.__class__.__name__
        dict_instance["created_at"] = self.created_at.isoformat()
        dict_instance["updated_at"] = self.updated_at.isoformat()

        return dict_instance

    def __str__(self):
        """
        Returns a string representation of an object
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
