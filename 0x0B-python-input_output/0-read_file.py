#!/usr/bin/python3
""" contains read_file function"""


def read_file(filename=""):
    """reads and prints a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
