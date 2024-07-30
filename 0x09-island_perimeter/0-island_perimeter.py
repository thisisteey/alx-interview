#!/usr/bin/python3
"""Module to calculate the perimeter of an island in a grid"""


def island_perimeter(grid):
    """Calculate the perimeter of an island without internal water bodies"""
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    nr = len(grid)
    for rx, currRow in enumerate(grid):
        nc = len(currRow)
        for cx, currCell in enumerate(currRow):
            if currCell == 0:
                continue
            borderSides = (
                rx == 0 or (len(grid[rx - 1]) > cx and grid[rx - 1][cx] == 0),
                cx == nc - 1 or (nc > cx + 1 and currRow[cx + 1] == 0),
                rx == nr - 1 or (
                    len(grid[rx + 1]) > cx and grid[rx + 1][cx] == 0),
                cx == 0 or currRow[cx - 1] == 0
            )
            perimeter += sum(borderSides)
    return perimeter
