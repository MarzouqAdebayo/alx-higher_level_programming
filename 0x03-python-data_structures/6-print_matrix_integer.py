#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        str = ""
        for j in i:
            str += " {:d}".format(j)
        str = str.strip()
        print("{}".format(str))
