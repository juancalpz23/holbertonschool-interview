#!/usr/bin/python3
"""
N Queens Problem Solver
Solves the N Queens problem using backtracking and prints all solutions.
"""

import sys


def solve_nqueens(N):
    """Solve the N Queens problem for a given board size."""
    def is_safe(board, row, col):
        """Check if placing a queen at (row, col) is safe."""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row, board):
        """Recursively solve the N Queens problem."""
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return

        for col in range(N):  # Try columns in ascending order
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1  # Reset

    solutions = []
    solve(0, [-1] * N)
    return solutions


def main():
    """Main entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
