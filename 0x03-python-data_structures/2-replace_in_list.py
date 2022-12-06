#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for char in my_list:
        if idx < 0:
            return my_list
        if idx > (len(my_list) - 1):
            return my_list
        if idx == char:
            my_list[char] = element
            return my_list
