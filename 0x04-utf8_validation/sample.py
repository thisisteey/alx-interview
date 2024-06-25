#!/usr/bin/python3
"""Module to check if a list of integers are valid UTF-8 code points"""


def validUTF8(data):
    """Checks if a data (list of integers) has a valid UTF-8 encoding"""
    for numberBytes in data:
        if numberBytes >> 7 == 0:
            continue
        elif numberBytes >> 5 == 0b110:
            continue
        elif numberBytes >> 4 == 0b1110:
            continue
        elif numberBytes >> 3 == 0b11110:
            continue
        else:
            return False
    return True
