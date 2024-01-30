#!/usr/bin/python3
"""
The "3-rectangle module"

The module contains class "Rectangle"
"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Gets the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints a friendly string"""
        rep = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                rep += "#" * self.__width
                if i < self.__height - 1:
                    rep += "\n"
        return rep

    def __repr__(self):
        """prints class friendly string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
