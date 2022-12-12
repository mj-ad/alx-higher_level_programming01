#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        length = len(sentence)
        first = sentence[0]
        tuple_c = (length, first)
        return tuple_c
    else:
        length = 0
        first = None
        tuple_c = (length, first)
        return tuple_c
