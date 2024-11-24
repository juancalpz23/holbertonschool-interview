#!/usr/bin/env python3

"""
N-Queens problem solver

This module solves the N-Queens problem using backtracking and prints
all possible solutions for a given `N` (size of the chessboard).

Usage:
    ./0-nqueens.py N.

Where:
    N must be an integer greater than or equal to 4
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
        board (list of list of int): The chessboard
        row (int): The row index to check
        col (int): The column index to check
        n (int): The size of the chessboard

    Returns:
        bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursively solve the N-Queens problem

    Args:
        board (list of list of int): The chessboard
        col (int): The current column to place a queen
        n (int): The size of the chessboard
        solutions (list of list of list of int): List to store all solutions
    """
    if col >= n:
        # Save the current solution in the required format
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(n):
    """
    Solve the N-Queens problem and print all solutions

    Args:
        n (int): The size of the chessboard
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
