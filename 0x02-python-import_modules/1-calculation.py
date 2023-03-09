#!/usr/bin/python3
from add, sub, mul, div import calculator_1.py

a = 10
b = 5
if __name__ == "__main__":
	print(f"{a} + {b} = {add(a, b)}")
	print(f"{a} - {b} = {sub(a, b)}")
	print(f"{a} * {b} = {mul(a, b)}")
        print(f"{a} / {b} = {div(a, b)}")
