#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = []
    od_set.extend([i for i in set_1 if i not in set_2])
    od_set.extend([i for i in set_2 if i not in set_1])
    return od_set
