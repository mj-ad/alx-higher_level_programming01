#!/usr/bin/python3
""" is_same_class function """

def is_same_class(obj, a_class):
    """ returns true if type(obj) and a_class are equal
    and false otherwise """


    if type(obj) == a_class:
        return True
    return False
