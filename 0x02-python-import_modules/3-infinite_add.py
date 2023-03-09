#!/usr/bin/python3
from sys import argv


def infinite_add():
    if len(argv) - 1 < 1:
        print("0")
    else:
        sum, i = 0, 1
        while i < len(argv):
            sum += int(argv[i])
            i += 1
        print(sum)


if __name__ == "__main__":
    infinite_add()
