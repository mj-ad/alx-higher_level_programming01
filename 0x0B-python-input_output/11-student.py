#!/usr/bin/python3
""" class Student """


class Student:
    """ class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and all(type(s) == str for s in attr):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return vars(self)

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
