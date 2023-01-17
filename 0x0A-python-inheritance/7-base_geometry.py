#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ Integer Validator """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value < 0 or value == 0:
            raise ValueError(f'{name} must be greater than 0')
