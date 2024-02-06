#!/usr/bin/python3
""" Contains the "save_to_json_file" function"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json writes a json object to a file

    Args:
        my_obj (object): JSON object
        filename (string): path to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
