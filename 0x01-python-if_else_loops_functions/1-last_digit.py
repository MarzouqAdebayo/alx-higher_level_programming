#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
last_digit = abs(number) % 10 * sign
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit:d} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit:d} and is less than 6 and"
          " not 0")
