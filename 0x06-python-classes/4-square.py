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

    def area(self):
        """Calculates the area of the square

        Returns: area of the square
        """
        return self.__size**2

    @property
    def size(self):
        """Gets the size attribute

        Returns: __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute

        Returns: none
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
