#!/usr/bin/python3
from sys import argv

def print_argv():
    i = 0
    for j in argv:
        if j == 0:
            continue
        print(f"{i}: {j}")
        i += 1

if __name__ == "__main__":
    if len(argv) - 1 == 1:
        print("{} argument".format(len(argv) - 1))
        print_argv()
    elif len(argv) - 1 == 0:
        print("{} arguments".format(len(argv) - 1))
    else:
        print("{} arguments".format(len(argv) - 1))
        print_argv()
