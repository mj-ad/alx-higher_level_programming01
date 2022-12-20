#!/usr/bin/python3
def safe_print_division(a, b):
    while True:
        if b != 0:
            try:
                a/b
            except ZeroDivisionError:
                print('Inside result: {}'.format('None'))
                return None
            finally:
                print('Inside result: {}'.format(a/b))
                return a/b
        else:
            print('Inside result: {}'.format('None'))
            return None
