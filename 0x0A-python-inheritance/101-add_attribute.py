#!/usr/bin/python3
""" "101-add_attribute" module"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
