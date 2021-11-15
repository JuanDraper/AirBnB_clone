#!/usr/bin/python3
"""test"""

import unittest
from models.amenity import Amenity
import os


class Test_Amenity(unittest.TestCase):
    """"test """

    def test_setUp(self):
        """ tests"""
        pass

    def test_tearDown(self):
        """"tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docstring(self):
        """test"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_args(self):
        """test"""
        b = Amenity(8)
        self.assertEqual(type(b).__name__, "Amenity")
        self.assertFalse(hasattr(b, "8"))
