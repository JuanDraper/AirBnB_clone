#!/usr/bin/python3
"""Unittest cases for User"""

import unittest
from models.user import User


class test_User(unittest.TestCase):
    """"Class User -Unittest """

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_args(self):
        """Arguments to the instance"""
        b = User(8)
        self.assertEqual(type(b).__name__, "User")
        self.assertFalse(hasattr(b, "8"))
