#!/usr/bin/python3
""" Contains "load_from_json_file" function"""


import json


def load_from_json_file(filename):
    """load_from_json_file load json from file filename

    Args:
        filename (str): path to file filename
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
