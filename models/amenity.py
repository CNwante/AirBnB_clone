#!/usr/bin/python3

"""
Amenity Module to create a amenity class for our hbnb project
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class to store the amenities of users


    Attributes:
        name (str): name

    Methods:
        None
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class as well as its super class
        """
        super().__init__(*args, **kwargs)

    pass
