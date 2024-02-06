#!/usr/bin/python3
"""Contains "to_json_string" function"""


import json


def to_json_string(my_obj):
    """to_json_string converts obj to JSON

    Args:
        my_obj (object): object to be converted to JSON string
    """
    return json.dumps(my_obj)
