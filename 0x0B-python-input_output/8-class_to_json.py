#!/usr/bin/python3
""" Contains "class_to_json" function"""


def class_to_json(obj):
    """class_to_json returns the dictionary description of obj

    Args:
        obj (object): obj

    Returns:
        dict object: object dictionary description
    """
    return obj.__dict__
