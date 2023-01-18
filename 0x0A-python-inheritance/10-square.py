#!/usr/bin/python3
""" class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """ inherits from class rectangle """

    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)

    def area(self):
        return self.__size ** 2
