#!/usr/bin/python3

""" A class Square that defines a square """


class Square:
    """ Attributes:
            size (int): Exception
            value (int): Exception
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            print('size must be an integer', end='')
            raise TypeError
        if size < 0:
            print('size must be >= 0', end='')
            raise ValueError

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            print('size must be an integer', end='')
            raise TypeError
        if value < 0:
            print('size must be >= 0', end='')
            raise ValueError

    def area(self):
        return self.__size ** 2
