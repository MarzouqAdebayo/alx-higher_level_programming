#!/usr/bin/python3
def no_c(my_string):
    arr = my_string.split(' ')
    for letter in arr:
        if (letter in 'cC'):
            arr[arr.index(letter)] = ""
    return " ".join(arr)
