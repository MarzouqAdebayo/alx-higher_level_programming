#!/usr/bin/python3
""" The "4-inherits_from.py" module
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class; otherwise False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
