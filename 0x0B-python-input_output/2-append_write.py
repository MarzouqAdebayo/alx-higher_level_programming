#!/usr/bin/python3
""" contains function that appends to file
"""


def write_file(filename="", text=""):
    """ appends some text to a file and
    returns the number of characters added

    Args:
        filename (str): The name of the file
        text (str): The text to append to file

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
