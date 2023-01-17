#!/usr/bin/python3
""" is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance of a_class
    and false otherwise """

    if isinstance(obj, a_class):
        return True
    return False
