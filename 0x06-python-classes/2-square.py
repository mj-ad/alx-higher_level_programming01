#!/usr/bin/python3

""" A class Square that defines a square """


class Square:
    """ Attributes:
            size (int): TypeError
    """
    def __init__(self, size=0):
        self.__size = size
        if int(size) != size:
            print('size must be an integer', end='')
            raise TypeError
        if size < 0:
            print('size must be >= 0', end='')
            raise ValueError
