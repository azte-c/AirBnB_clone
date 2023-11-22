#!/bin/usr/python3
""""""
import uuid
from datetime import datetime
time_form = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """base model class"""

    def __init__(self):
        """initializing the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string rep of class"""
        return f"({self.__class__.__name__}) ({self.id}) {self.__dict__}"

    def save(self):
        """update updated_at to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary containing keys and values"""
        obj_dict = self.__dict__.copy() 
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime(time_form)
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
