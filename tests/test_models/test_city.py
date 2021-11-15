#!/usr/bin/python3
"""Unittesty"""

import unittest
from models.city import City


class test_City(unittest.TestCase):
    """"Test for City class"""

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = City()
        self.assertIsInstance(obj, City)

    def test_args(self):
        """Test arguments"""
        b = City(8)
        self.assertEqual(type(b).__name__, "City")
        self.assertFalse(hasattr(b, "8"))
