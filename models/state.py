#!/usr/bin/python3

"""
State Module to create a state class for our hbnb project
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class to store the States of users


    Attributes:
        name (str): name of the state

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
