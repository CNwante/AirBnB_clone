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
        updated_at (datetime): assign datetime every time object is updated

    Methods defined:

        __str__() -> None: print formatted string
        save() -> None : updates the instance attribute updated_at
        to_dict() -> dict : returns dict (keys and values of instance)

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
        self.id = None
        self.created_at = None
        self.updated_at = None

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

        if self.id is None:
            self.id = str(uuid.uuid4())

        if self.created_at is None:
            self.created_at = datetime.now()

        if self.updated_at is None:
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Prints a formaatted string to stdout

        Args:
            None

        Return:
            string format
        """
        str_name = type(self).__name__

        return "[{}] ({}) {}".format(str_name, self.id, self.__dict__)

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

        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = created_format
        new_dict["updated_at"] = updated_format

        return new_dict
