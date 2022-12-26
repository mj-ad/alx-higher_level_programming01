#!/usr/bin/python3

""" A class Square that defines a square """


class Square:
    """ class Square """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        a = self.__size
        if a == 0:
            print()
        else:
            for i in range(0, a):
                for i in range(0, a):
                    print('#', end='')
                print()
