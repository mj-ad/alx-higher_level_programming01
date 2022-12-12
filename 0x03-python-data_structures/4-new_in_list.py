#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    for i in range(0, len(my_list)):
        if idx < 0:
            return new_list
        if idx > (len(my_list) - 1):
            return new_list
        if idx == i:
            new_list[i] = element
            return new_list
