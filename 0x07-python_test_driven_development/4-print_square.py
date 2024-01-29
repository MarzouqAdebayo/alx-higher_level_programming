#!/usr/bin/python3
"""
The "4-print_square" module

The module contains one function "print_square"
"""


def print_square(size=""):
    """
    Prints a square with the # character
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
