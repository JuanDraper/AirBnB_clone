#!/usr/bin/python3
"""Unittestl"""

import unittest
from models.base_model import BaseModel
from models import storage
import os
import uuid


class Test_BaseModel(unittest.TestCase):
    """tes """

    def test_setUp(self):
        """ tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_tearDown(self):
        """" tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docstring(self):
        """test"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_v4_uuid(self):
        """Test """
        obj = BaseModel()
        test_uuid = uuid.UUID(obj.id, version=4)
        self.assertEqual(str(test_uuid), obj.id, "Error: Different version")

    def test_args(self):
        """test"""
        b = BaseModel(8)
        self.assertEqual(type(b).__name__, "BaseModel")
        self.assertFalse(hasattr(b, "8"))

    def test_str(self):
        """test"""
        b = BaseModel()
        printb = b.__str__()
        self.assertEqual(printb,
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_save(self):
        """Test"""
        obj = BaseModel()
        obj.save()
        key = "BaseModel.{}".format(obj.id)
        comp = storage._FileStorage__objects[key]
        self.assertEqual(obj.id, comp.id)
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        """Test"""
        obj = BaseModel()
        new_dict = obj.__dict__.copy()
        new_dict["__class__"] = obj.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        comparing = obj.to_dict()
        self.assertDictEqual(new_dict, comparing)
