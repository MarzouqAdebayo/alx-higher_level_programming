#!/usr/bin/python3
""" Contains Student class"""


class Student:
    """Defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """__init__ initializes the class instance

        Args:
            first_name (string): firstname string argument
            last_name (string): lastname string argument
            age (int): age int argument
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrives the dictionary description of
        Student class instance
        """
        return self.__dict__
