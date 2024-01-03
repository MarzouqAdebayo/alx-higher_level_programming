#!/usr/bin/python3
def uppercase(c):
    for letter in c:
        diff = 0
        if 97 <= ord(letter) < 97 + 26:
            diff = 32
        else:
            diff = 0
        print("{}".format(chr(ord(letter) - diff)), end="")
    print("")
