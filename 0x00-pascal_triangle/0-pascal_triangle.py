#!/usr/bin/python3
"""Module for generating Pascal's triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n levels
    Args:
    n (int): The number of levels of the triangle
    Returns:
    list: list of lists of integers representing triangle"""
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for lvl in range(n):
        row = []
        for idx in range(lvl + 1):
            if idx == 0 or idx == lvl:
                row.append(1)
            else:
                row.append(triangle[lvl - 1][idx - 1] + triangle[lvl - 1][idx])
        triangle.append(row)
    return triangle
