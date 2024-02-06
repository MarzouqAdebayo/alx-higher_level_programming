#!/usr/bin/python3
""" Contains the "pascal_triangle" function"""


def pascal_triangle(n: int):
    """pascal_triangle generates a pascal triangle

    Args:
        n (int): height of the pascal triangle

    Returns:
        2D array: An array of array representing the pascal triangle
    """
    if n <= 0:
        return []
    outer_array = [[1]]
    if n == 1:
        return outer_array
    for i in range(1, n):
        inner_array = []
        previous_array = outer_array[i - 1]
        last_val = 0
        loop_val = (i // 2) + 1
        for j in range(loop_val):
            val = last_val + previous_array[j]
            inner_array.append(val)
            last_val = previous_array[j]
        if i % 2 == 0:
            temp = inner_array[:-1]
            outer_array.append(inner_array + temp[::-1])
        else:
            outer_array.append(inner_array + inner_array[::-1])
    return outer_array
