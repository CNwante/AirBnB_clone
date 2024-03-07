#!/usr/bin/python3

"""
Module for testing the FileStorage Class in the models directory
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test FIleStorage class saved in models/engne
    """

    def setUp(self):
        """
        File Storage SetUp()
        """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.base_model.name = "My_First_Model"
        self.base_model.my_number = 89

    def tearDown(self):
        """
        Tear Down
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        Tests all method
        """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """
        Test new method
        """
        self.storage.new(self.base_model)
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + self.base_model.id, all_objs)

    def test_save_reload(self):
        """
        Test reload function
        """
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn("BaseModel." + self.base_model.id, all_objs)
        loaded_model = all_objs["BaseModel." + self.base_model.id]
        self.assertIsInstance(loaded_model, dict)


if __name__ == "__main__":
    unittest.main()
