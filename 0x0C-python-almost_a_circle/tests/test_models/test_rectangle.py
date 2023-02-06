#!/usr/bin/python3
""" Testing class Rectangle """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Testing instantiation """

    def test_two_arg(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(8, 9)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_after_unique_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 0, 0, 7)
        r3 = Rectangle(8, 9)
        self.assertEqual(r1.id, r3.id - 1)

    def test_unique_id(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)
