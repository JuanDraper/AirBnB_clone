#!/usr/bin/python3
"""Unittest"""

import unittest
from models.place import Place


class test_Place(unittest.TestCase):
    """Test for Clase Place"""

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_args(self):
        """Test arguments"""
        b = Place(8)
        self.assertEqual(type(b).__name__, "Place")
        self.assertFalse(hasattr(b, "8"))
