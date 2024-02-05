#!/usr/bin/python3
""" The "3-is_kind_of_class.py" module
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False"""
    return isinstance(obj, a_class)
