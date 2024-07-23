#!/usr/bin/python3
"""Module for performing in-place rotation of a 2D matrix"""


def rotate_2d_matrix(matrix):
    """In-place rotation of a rectangular 2D list (matrix)"""
    size = len(matrix[0])
    for col in range(size - 1, -1, -1):
        for row in range(size):
            matrix[row].append(matrix[col].pop(0))
