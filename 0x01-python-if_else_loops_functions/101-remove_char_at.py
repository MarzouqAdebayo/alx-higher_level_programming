#!/usr/bin/python3
def remove_char_at(str, n):
    arr = []
    res = ""
    for i in range(len(str)):
        if (i == n):
            continue
        arr.append(str[i])
    return res.join(arr)
