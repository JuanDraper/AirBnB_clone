#!/usr/bin/python3
"""Unittest cases for review"""

import unittest
from models.review import Review


class test_review(unittest.TestCase):
    """"Unittest for Class Review"""

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_args(self):
        """Arguments to the instance"""
        b = Review(8)
        self.assertEqual(type(b).__name__, "Review")
        self.assertFalse(hasattr(b, "8"))
