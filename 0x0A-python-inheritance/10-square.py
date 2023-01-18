#!/usr/bin/python3
""" class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """ inherits from class rectangle """

    def __init__(self, size):
        """ initialization """
        
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area of a square """
        
        return self.__ size ** 2
