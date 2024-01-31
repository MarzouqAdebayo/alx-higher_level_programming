#!/usr/bin/python3
"""
The "2-matrix_divided" module

The module contains one function "matrix_divided"
"""


def matrix_divided(matrix=[0], div="string"):
    """
    Returns a + b
    """

    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/"
            "floats"
        )
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        temp = []
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    " integers/floats"
                )
            temp.append(round(col / div, 2))
        new_matrix.append(temp)

    return new_matrix
