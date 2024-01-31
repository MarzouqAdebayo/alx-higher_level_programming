#!/usr/bin/python3
"""
The "0-add_integer" module

The module contains one function "add_integer"
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    x = [float("inf"), float("-inf")]
    if (not isinstance(a, int) and not isinstance(a, float)) or a in x:
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)) or b in x:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
