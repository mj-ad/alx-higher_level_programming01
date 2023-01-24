#!/usr/bin/python3
""" Function read_file """


def read_file(filename=""):
    """Reads text file UTF8 and prints to stdout """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
