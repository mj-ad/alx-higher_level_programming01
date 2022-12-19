#!/usr/bin/python3
def safe_print_integer(value):
    while True:
        try:
            int(value) == value
            print('{:d}'.format(value))
            return True
        except ValueError:
            return False
