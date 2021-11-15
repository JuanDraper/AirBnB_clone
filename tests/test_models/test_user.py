#!/usr/bin/python3
"""Unittest cases for User"""

import unittest
from models.user import User
import os


class Test_User(unittest.TestCase):
    """"Class User -Unittest """

    def test_setUp(self):
        """SetUps tests"""
        passi

    def test_tearDown(self):
        """"Restart tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_args(self):
        """Arguments to the instance"""
        b = User(8)
        self.assertEqual(type(b).__name__, "User")
        self.assertFalse(hasattr(b, "8"))
