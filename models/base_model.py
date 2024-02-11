#!/usr/bin/python3
"""Define BaseModel class."""

from datetime import datetime
import json
import uuid

class BaseModel:
    """Initialise the class"""
    def __init__(self,):
        """

        """
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
    
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """

        """
        dict_instance = self.__dict__.copy()
        dict_instance["__class__"] = self.__class__.__name__
        dict_instance["created_at"] = self.created_at.isoformat()
        dict_instance["updated_at"] = self.updated_at.isoformat()

        return dict_instance

    def __str__(self):
        """

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
