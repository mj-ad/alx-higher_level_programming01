#!/usr/bin/python3

""" A class Square that defines a square  """


class Square:
    """ class Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__position = position
        if type(position) != tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or type(value[0]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[1]) != int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        a = self.__size
        b = self.__position
        if a == 0:
            print()
        else:
            print('\n' * b[1], end='')
            for i in range(0, a):
                print(' ' * b[0], end='')
                for i in range(0, a):
                    print('#', end='')
                print()
