#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operators = "+-*/"
    a = argv[1]
    op = argv[2]
    b = argv[3]
    if len(argv) != 4:
        exit(1)
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if (op == "+"):
        print("{} {} {} = {}".format(a, op, b, add(int(a), int(b))))
    if (op == "-"):
        print("{} {} {} = {}".format(a, op, b, sub(int(a), int(b))))
    if (op == "*"):
        print("{} {} {} = {}".format(a, op, b, mul(int(a), int(b))))
    if (op == "/"):
        print("{} {} {} = {}".format(a, op, b, div(int(a), int(b))))
