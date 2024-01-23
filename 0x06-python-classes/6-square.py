#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square object

    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square object

        Args:
            size (int): size of the square
            position (tuple): print position of the square

        Returns: None
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter of __position

        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position

        Args:
            value (tuple): position of the square in 2D space

        Returns:
            None
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or value[0] < 0
            or not isinstance(value[1], int)
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the area of the square with #

        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for z in range(self.__size)]))
