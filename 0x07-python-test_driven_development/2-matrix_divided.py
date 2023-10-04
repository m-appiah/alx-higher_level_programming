#!/usr/bin/python3
"""
Module for a Matrix division function
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists (matrix)- type can be ints or floats
        div: Divisor (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        The representation of new matrix
    """
    if not all(
            isinstance(row, list) and
            all(isinstance(val, (int, float)) for val in row)
            for row in matrix
            ):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
