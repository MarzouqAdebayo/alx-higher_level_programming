#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    for k in new:
        print("{}: {}".format(k, new[k]))
