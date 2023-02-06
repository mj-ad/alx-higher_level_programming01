#!/usr/bin/python3
""" Testing class Rectangle """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Testing instantiation """

    def test_two_arg(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_after_unique_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 0, 0, 7)
        r3 = Rectangle(8, 9)
        self.assertEqual(r1.id, r3.id - 1)

    def test_unique_id(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def testtwo_arg(self):
        self.assertEqual(2, Rectangle(10, 2).height)

    def test_three_arg(self):
        r1 = Rectangle(10, 2, 9)
        self.assertEqual(10, r1.width)

    def test_four_arg(self):
        self.assertEqual(0, Rectangle(10, 2, 0, 0).x)

class Test_Rectangle_Validation(unittest.TestCase):
    """ validating setter methods """
    
    def test_string_arg(self):
        with self.assertRaises(TypeError):
            print(Rectangle('1', 2).width)

    def test_second_string_arg(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, '2').height)

    def test_third_string_arg(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, 2, '3').x)

    def test_fourth_string_arg(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, 2, 3, '4').y)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            print(-1, Rectangle(-1, 2).width)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            print(-2, Rectangle(1, -2).height)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            print(0, Rectangle(1, 0).height)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            print(0, Rectangle(0, 2).width)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            print(-3, Rectangle(1, 2, -3).x)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            print(-4, Rectangle(1, 2, 3, -4).y)

if __name__ == "__main__":
    unittest.main()
