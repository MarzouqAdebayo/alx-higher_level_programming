#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square object

    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0):
        """Initializes a Square object

        Args:
            size (int): size of the square

        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
