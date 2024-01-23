#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Square class defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a square.
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        position (property): Getter method for the position attribute.
        position (setter): Setter method for the position attribute.
        area(self): Returns the area of the square.
        my_print(self): Prints the square in stdout with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square

        Args:
            size (int): size of a side of the square
            position (tuple): positoin of the square in 2D space

        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area

        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            value (int): size of a side of the square

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

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
        else:
            self.__position = value

    def __str__(self):
        """prints the square

        Returns:
            None
        """
        result = ""
        if self.__size == 0:
            return result
        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result
