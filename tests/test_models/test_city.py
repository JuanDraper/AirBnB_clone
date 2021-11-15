#!/usr/bin/python3
"""Unittesty"""

import unittest
from models.city import City
import os


class Test_City(unittest.TestCase):
    """"city test"""

    def test_setUp(self):
        """test"""
        pass

    def test_tearDown(self):
        """test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docstring(self):
        """test"""
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test """
        obj = City()
        self.assertIsInstance(obj, City)

    def test_args(self):
        """test"""
        b = City(8)
        self.assertEqual(type(b).__name__, "City")
        self.assertFalse(hasattr(b, "8"))
