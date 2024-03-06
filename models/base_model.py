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

    def __init__(self, id=None, created_at=None, updated_at=None):

        """
        Initializes the BaseModel class

        Args:
            None

        Return:
            None
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at


    def __str__(self):
        """
        Prints a formaatted string to stdout

        Args:
            None

        Return:
            string format
        """

        return '[{}] (<{}>) <{}>'.format(self.__name__,
                self.id, self.__dict__)
