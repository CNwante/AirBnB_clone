#!/usr/bin/python3

"""
City Module to create a city class for our hbnb project
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class to store the cities of users


    Attributes:
        name (str): name of the city
        state_id (str): the id of the state

    Methods:
        None
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class as well as its super class
        """
        super().__init__(*args, **kwargs)
        state_id = self.id

    pass
