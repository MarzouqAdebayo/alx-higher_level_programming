#!/usr/bin/python3
""" contains function that writes to file
"""


def write_file(filename="", text=""):
    """ writes some text to a file and
    returns the number of characters written

    Args:
        filename (str): The name of the file
        text (str): The text to write to file

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
