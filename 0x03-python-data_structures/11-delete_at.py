#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(0, len(my_list)):
        if idx < 0:
            return my_list
        if i == idx:
            c = my_list[i]
            my_list.remove(c)
            return my_list
