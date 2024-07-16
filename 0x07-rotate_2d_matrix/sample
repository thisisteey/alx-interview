#!/usr/bin/python3
"""Module for performing in-place rotation of a 2D matrix"""


def rotate_2d_matrix(matrix):
    """In-place rotation of a rectangular 2D list (matrix)"""
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda row: type(row) == list, matrix)):
        return
    rowCount = len(matrix)
    colCount = len(matrix[0])
    if not all(map(lambda row: len(row) == colCount, matrix)):
        return
    currCol, currRow = 0, rowCount - 1
    for idx in range(colCount * rowCount):
        if idx % rowCount == 0:
            matrix.append([])
        if currRow == -1:
            currRow = rowCount - 1
            currCol += 1
        matrix[-1].append(matrix[currRow][currCol])
        if currCol == colCount - 1 and currRow >= -1:
            matrix.pop(currRow)
        currRow -= 1
