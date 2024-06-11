#!/usr/bin/python3
"""Module defined for minimum operations function minOperations"""


def minOperations(n):
    """Calculates the minimum number of operations required to transform
    a single character 'H' in a text file into exactly 'n'
    Args:
    n int: the target number of H characters to get in the text file"""
    if type(n) is not int:
        return 0
    ops_count = 0
    copied_content = 0
    curr_count = 1
    while curr_count < n:
        if copied_content == 0:
            copied_content = curr_count
            curr_count += copied_content
            ops_count += 2
        elif n - curr_count > 0 and (n - curr_count) % curr_count == 0:
            copied_content = curr_count
            curr_count += copied_content
            ops_count += 2
        elif copied_content > 0:
            curr_count += copied_content
            ops_count += 1
    return ops_count
