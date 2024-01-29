#!/usr/bin/python3
"""
The "3-say_my_name" module

The module contains one function "say_my_name"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string which contains first_name and last_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
