#!/usr/bin/python3

"""
This Module handles file storage of the BaseModel Object

The class ``FileStorage`` is created to manage the saving
and retrieving of data from the BaseModel class
"""

import json
import os


class FileStorage:
    """
    This class handles storing of data into files
    It handles the serialization and deserialization of JSON files
    to instances (BaseModel)

    Attributes:
        Class:
            __file_path (str): path to the JSON file
            __objects (dict): store all objects based on id

    Methods:
        all(self) -> (dict): return __objects
            Param:
                None
            Return:
                __objects

        new(self, obj) -> None:
            Param:
                obj: objects
            Return:
                None

        save(self) -> None: serializes __objects to JSON file
            Param:
                None
            Return:
                None

        reload(self) -> None: deserializes JSON file to __objects
            Param:
                None
            Return:
                None
    """

    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """
        Initializes the FileStorage class

        Args:
            None

        Param:
            None
        """
        pass

    def all(self):
        """
        Returns the __object class attribute

        Param:
            None
        Return:
            None
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Create a dict and sets the obj.id as key

        Param:
            obj (obj): the obj
        Return:
            None
        """
        key = type(obj).__name__ + "." + obj.id
        value = obj.to_dict()
        FileStorage.__objects[key] = value

    def save(self):
        """
        Serializes __objects to JSON file to __file_path

        Param:
            None
        Return:
            None
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file, indent=4, sort_keys=True)

    def reload(self):
        """
        Deserializes __objects from JSON file in __file_path

        Param:
            None
        Return:
            None
        """

        file_name = FileStorage.__file_path
        new_dict = dict()
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                try:
                    new_obj = json.load(file)
                    for key, value in new_obj.items():
                        new_dict[key] = value
                except json.JSONDecodeError:
                    pass

        FileStorage.__objects = new_dict
