#!/usr/bin/python3
""" Contains "from_json_string" function"""


import json


def from_json_string(my_str):
    """from_json_string converts JSON string to object

    Args:
        my_str (str): JSON string

    Returns:
        (object): python object
    """
    return json.loads(my_str)
