#!/usr/bin/python3
""" Defines unittests for base.py """

import unittest
from models.base import Base

class Base_test(unittest.TestCase):
    """ Testing Base class """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_same_as_id(self):
        b1 = 12
        b2 = Base(12)
        self.assertEqual(b1, b2.id)

    def test_no_arg_after_unique_id(self):
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

if __name__ == "__main__":
    unittest.main()
