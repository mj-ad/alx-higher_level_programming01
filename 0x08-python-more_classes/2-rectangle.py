#!/usr/bin/python3

""" class Rectangle """


class Rectangle:
    """ Rectangle """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    def area(self):
        a = self.__width
        b = self.__height
        return a * b

    def perimeter(self):
        a = self.__width
        b = self.__height
        return ((2 * a) + (2 * b))
