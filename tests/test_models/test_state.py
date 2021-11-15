#!/usr/bin/python3
"""Unittest cases for Amenity"""

import unittest
from models.state import State


class test_State(unittest.TestCase):
    """"Class State -Unittest """

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_args(self):
        """Arguments to the instance"""
        b = State(8)
        self.assertEqual(type(b).__name__, "State")
        self.assertFalse(hasattr(b, "8"))
