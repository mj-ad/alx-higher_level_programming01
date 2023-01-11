#!/usr/bin/pythonn3

""" class Rectangle """


class Rectangle:
    """ Draws a rectangle """
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
        return self.height * self.width

    def perimeter(self):
        a = self.__width
        b = self.__height
        if a == 0:
            b = 0
        if b == 0:
            a = 0
        return ((2 * a) + (2 * b))

    def __str__(self):
        d = ''
        a = self.__width
        b = self.__height
        if a != 0 and b != 0:
            for i in range(0, b):
                d += '#' * a
                if i != self.__height - 1:
                    d += '\n'
            return d
        return d
