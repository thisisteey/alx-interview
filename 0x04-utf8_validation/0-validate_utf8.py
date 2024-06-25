#!/usr/bin/python3
"""Module to check if a list of integers are valid UTF-8 code points"""


def validUTF8(data):
    """Checks if a data (list of integers) has a valid UTF-8 encoding"""
    remBytes = 0
    startMask = 1 << 7
    contMask = 1 << 6

    for numBytes in data:
        currMask = 1 << 7
        if remBytes == 0:
            while currMask & numBytes:
                remBytes += 1
                currMask = currMask >> 1
            if remBytes == 0:
                continue
            if remBytes == 1 or remBytes > 4:
                return False
        else:
            if not (numBytes & startMask and not (numBytes & contMask)):
                return False
        remBytes -= 1
    if remBytes == 0:
        return True
    return False
