#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    check = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0
    prev = roman_string[0]
    current = roman_string[0]
    for current in roman_string:
        if (current not in check.keys()):
            return 0
        if check[prev] < check[current]:
            total -= 2 * check[prev]
            total += check[current]
        else:
            total += check[current]
        prev = current
    return total
