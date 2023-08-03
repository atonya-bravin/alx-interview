#!/usr/bin/python3
"""Solving N Queens with Backtracking"""


import sys


def is_safe_to_place_queen(row, col, placed_queens):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    Returns True if there are no conflicts with previously placed queens.
    """
    for queen_row, queen_col in placed_queens:
        if col == queen_col or\
                row - col == queen_row - queen_col or\
                col - queen_col == queen_row - row:
            return False
    return True


def solve_nqueens(board_size, current_row, placed_queens):
    """
    Solve the N-Queens problem by placing queens on an N by N board so that
    no queens are attacking each other.
    Parameters:
        board_size: An integer that sets the board size
                    and the number of queens.
        current_row: The current row being considered for queen placement.
        placed_queens: The current state of the board
                    represented as a list of queen positions.
    """
    if current_row == board_size:
        # If we have placed queens in all rows (reached the end of the board)
        # print the solution.
        print(placed_queens)
    else:
        for col in range(board_size):
            if is_safe_to_place_queen(current_row, col, placed_queens):
                # If it's safe to place a queen at position (current_row, col)
                # add it to the board.
                placed_queens.append((current_row, col))
                # Proceed to the next row by making a recursive call.
                solve_nqueens(board_size, current_row + 1, placed_queens)
                # Backtrack and remove the last queen placement
                # to explore other possibilities.
                placed_queens.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(board_size, 0, [])


if __name__ == '__main__':
    main()
