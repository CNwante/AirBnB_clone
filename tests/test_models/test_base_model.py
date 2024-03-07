#!/usr/bin/python3

"""
Module to test every edge case of the base model class

"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Tests the BaseModel for any unseen error/failure that might occur

    SuperClass:
        unittest.TestCase
    """

    def test_instance_creation(self):
        """
        Test the instance creation
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_unique_id(self):
        """
        Test the unique id
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        """
        Test the attribute creation or rep
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        test_dict = my_model.__dict__
        self.assertEqual(
            str(my_model), "[BaseModel] ({}) {}".format(my_model.id, test_dict)
        )

    def test_save_method(self):
        """
        Test the save method
        """
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to dict method
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        iso_created_at = my_model.created_at.isoformat()
        iso_updated_at = my_model.updated_at.isoformat()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["name"], "My First Model")
        self.assertEqual(my_model_dict["my_number"], 89)
        self.assertEqual(my_model_dict["created_at"], iso_created_at)
        self.assertEqual(my_model_dict["updated_at"], iso_updated_at)

    def test_to_dict_datetime_format(self):
        """
        Test the datetime of the to_dict format
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(
            datetime.fromisoformat(my_model_dict["created_at"]), datetime
        )
        self.assertIsInstance(
            datetime.fromisoformat(my_model_dict["updated_at"]), datetime
        )

    def test_to_dict_id_str(self):
        """
        Test if id has been converted to str
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict["id"], str)
        self.assertEqual(my_model_dict["id"], str(my_model.id))

    def test_init_with_empty_dict(self):
        """
        Test init with empty dict
        """
        my_model = BaseModel()
        my_model_json = {}
        my_new_model = BaseModel(**my_model_json)

        self.assertIsInstance(my_new_model.id, str)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
