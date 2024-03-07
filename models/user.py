#!/usr/bin/python3

"""
Module for class ``user`` that inherits from ``BaseModel`` class

    To create a user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Creates a new user for our hbnb project (this inherits fro BaseModel)

    Attributes:
        email (str): email address of user
        password (str): password of user
        first_name (str): the first name of user
        last_name (str): the last name of user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """
        Initializes the ``User()`` class
        """
        pass
    pass


