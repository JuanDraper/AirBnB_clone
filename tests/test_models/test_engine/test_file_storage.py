#!/usr/bin/python3
"""Unittest cases for file storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import uuid


class Test_File_Storage(unittest.TestCase):
    """
    Class for testing File storage class.
    """

    def setUp(self):
        """SetUps tests"""
        self.storage = FileStorage()

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_save(self):
        """Testing the save function"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(self.storage._FileStorage__file_path)
        self.assertTrue(self.storage._FileStorage__objects)
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))
        key = "BaseModel.{}".format(obj.id)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertDictEqual(self.storage.all()[key].to_dict(), obj.to_dict())
