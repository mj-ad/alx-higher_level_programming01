#!/usr/bin/python3
""" Function write_file """


def write_file(filename="", text=""):
    """returns number of characters written"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
