#!/usr/bin/python3

"""
Review Module to create a review class for our hbnb project
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class to store the reviews of users


    Attributes:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): text of description

    Methods:
        None
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class as well as its super class
        """
        super().__init__(*args, **kwargs)
        state_id = self.id

    pass
