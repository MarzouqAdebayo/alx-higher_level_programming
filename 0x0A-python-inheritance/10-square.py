#!/usr/bin/python3
""" The '10-square' module
"""


BaseRectangle = __import__('9-rectangle').Rectangle


class Square(BaseRectangle):
    """ Square class inherits from Rectangle class
    """
    def __init__(self, size):
        """ Instantiates the Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
