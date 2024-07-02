#!/usr/bin/python3
"""N Queens algorithm using backtracking with recursion"""
import sys


class NQueens:
    """Class to solve N Queens algorithm problem"""

    def __init__(self, size):
        """Initialise the NQueens class"""
        self.size = size
        self.queenPos = [0 for pos in range(size + 1)]
        self.solutions = []

    def queen_placement(self, currPos, col):
        """Checks if the queen can be placed in a specific column"""
        for prevPos in range(1, currPos):
            if self.queenPos[prevPos] == col or \
                    abs(self.queenPos[prevPos] - col) \
                    == abs(prevPos - currPos):
                return 0
        return 1

    def nqueens(self, currPos):
        """Solve NQueens by trying to place on queens on board"""
        for col in range(1, self.size + 1):
            if self.queen_placement(currPos, col):
                self.queenPos[currPos] = col
                if currPos == self.size:
                    solution = []
                    for col in range(1, self.size + 1):
                        solution.append([col - 1, self.queenPos[col] - 1])
                    self.solutions.append(solution)
                else:
                    self.nqueens(currPos + 1)
        return self.solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueens(N)
solutions = queen.nqueens(1)

for col in solutions:
    print(col)
