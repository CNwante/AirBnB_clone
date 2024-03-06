#!/usr/bin/python3

"""
This Module handles file storage of the BaseModel Object

The class ``FileStorage`` is created to manage the saving
and retrieving of data from the BaseModel class
"""

class FileStorage:
    """
    This class handles storing of data into files
    It handles the serialization and deserialization of JSON files
    to instances (BaseModel)

    Attributes:
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
    pass
