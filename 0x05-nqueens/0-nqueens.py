#!/usr/bin/env python3
"""
This is a module that implements
a common interview question,
the NQueen problem
"""


import sys


def NQueenSol(total_queens):

    # tracks all the columns that contain a queen
    col = []

    # tracks the diagonal from the bottom left to top right
    negative_diag = []

    # tracks the diagonal from the top right to bottom left
    positive_diag = []

    # Contains all the valid states
    valid_states = []

    for row in range(int(total_queens)):
        for column in range(1, int(total_queens)):
            if column in col or\
                    row - column in negative_diag or\
                    row + column in positive_diag:
                continue
            else:
                col.append(column)
                negative_diag.append(row - column)
                positive_diag.append(row + column)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: nqueens N")
    else:
        NQueenSol(sys.argv[1])
