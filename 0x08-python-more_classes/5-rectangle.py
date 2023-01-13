#!/usr/bin/python3

""" class Rectangle """


class Rectangle:
    """ class Deletion """
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
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0:
            self.__height = 0
        if self.__height == 0:
            self.__width = 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        d = ''
        a = self.__width
        b = self.__height
        if a != 0 and b != 0:
            for i in range(0, b):
                d += '#' * a
                if i < b - 1:
                    d += '\n'
            return d
        return d

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
