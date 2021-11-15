#!/usr/bin/python3
"""Unittest"""

import unittest
from models.place import Place
import os


class Test_Place(unittest.TestCase):
    """place test"""

    def test_setUp(self):
        """tests"""
        pass

    def test_tearDown(self):
        """" tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docstring(self):
        """tests"""
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Tests"""
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_args(self):
        """test"""
        b = Place(8)
        self.assertEqual(type(b).__name__, "Place")
        self.assertFalse(hasattr(b, "8"))
