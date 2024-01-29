#!/usr/bin/python3
"""The "5-text_indentation module

Function:  text_indentation(text)
"""


def text_indentation(text):
    """ prints a text with 2 new lines after \
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if i == 0 and text[i] == " ":
            while i < len(text) and text[i] == " ":
                i += 1
        elif text[i] in ".?:":
            print(text[i], end="")
            print()
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
