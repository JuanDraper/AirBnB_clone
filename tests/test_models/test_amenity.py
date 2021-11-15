#!/usr/bin/python3
"""test"""

import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """Test for Class Amenity"""

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_args(self):
        """test arguments"""
        b = Amenity(8)
        self.assertEqual(type(b).__name__, "Amenity")
        self.assertFalse(hasattr(b, "8"))
