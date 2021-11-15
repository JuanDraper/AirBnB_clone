#!/usr/bin/python3
"""Unittest cases for review"""

import unittest
from models.review import Review
import os


class Test_Place(unittest.TestCase):
    """"Class Review -Unittest """

    def test_setUp(self):
        """SetUps tests"""
        pass

    def test_tearDown(self):
        """"Restart tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(Review.__doc__) > 1)
        self.assertTrue(len(Review.__init__.__doc__) > 1)
        self.assertTrue(len(Review.__str__.__doc__) > 1)
        self.assertTrue(len(Review.save.__doc__) > 1)
        self.assertTrue(len(Review.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_args(self):
        """Arguments to the instance"""
        b = Review(8)
        self.assertEqual(type(b).__name__, "Review")
        self.assertFalse(hasattr(b, "8"))
