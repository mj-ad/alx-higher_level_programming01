#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == len(tuple_b):
        new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
        return new_tuple
    if len(tuple_b) == 0:
        return tuple_a
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_a) > len(tuple_b):
        new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1]))
        return new_tuple
    if len(tuple_a) < len(tuple_b):
        new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_b[1]))
        return new_tuple
    if len(tuple_a) < len(tuple_b):
        new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_b[1]))
        return new_tuple
