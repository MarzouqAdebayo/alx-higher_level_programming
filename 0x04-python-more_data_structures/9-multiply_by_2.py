#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for val in a_dictionary.values():
        val *= 2
    return {key: val*2 for key, val in a_dictionary.items()}
