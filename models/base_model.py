#!/usr/bin/python3

"""
This module defines all the common attributes
and methods for other classes in our hbnb project
"""

import uuid
from datetime import datetime

class BaseModel:

    """
    BaseModel (parent class) for all the subclasses
    that will be derived hereafter.

    Attributes defined:

        id (str) : assign with an uuid when an instance is created
        created_at (datetime): assign current datetime when instance is created
        updated_at (datetime): assign current datetime every time object is updated

    Methods defined:

        __str__() -> None: print formatted string
        save() -> None : updates the instance attribute updated_at
        to_dict() -> dict : returns dict containing all keys and values of instance

    """

    def __init__(self, *args, **kwargs):

        """
        Initializes the BaseModel class

        Args:
            *args: list multiple args
            **kwargs: a list of keyword arguments

        Return:
            None
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """
        Prints a formaatted string to stdout

        Args:
            None

        Return:
            string format
        """

        return '[{}] ({}) {}'.format(type(self).__name__,
                self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute 

        Args:
            None

        Return:
            None
        """

        self.updated_at = datetime.now()
        pass


    def to_dict(self):
        """
        Create dictionary for attributes

        Args:
            None

        Return:
            None
        """

        updated_format = self.updated_at.isoformat()
        created_format = self.created_at.isoformat()

        new_dict = self.__dict__.copy()

        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = created_format
        new_dict['updated_at'] = updated_format

        return new_dict

        
    
