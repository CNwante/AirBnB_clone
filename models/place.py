#!/usr/bin/python3

"""
Place Module to create a place class for our hbnb project
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class to store the places


    Attributes:
        city_id (str): city.id
        user_id (str): User.id
        name (str): name
        description (str): description
        number_rooms (int): number of rooms
        number_bathrooms (int): num of bathrooms
        max_guest (int): max num of guest
        price_by_night (int): price per night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): list of amenities

    Methods:
        None
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitube = 0.0
    amenity_ids = list()

    def __init__(self, *args, **kwargs):
        """
        Initializes the class as well as its super class
        """
        super().__init__(*args, **kwargs)
        state_id = self.id

    pass
