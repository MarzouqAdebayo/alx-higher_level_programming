#!/usr/bin/python3
for i in range(26):
    case = 122
    if i % 2 == 0:
        case = 122
    else:
        case = 90
    print("{}".format(chr(case - i)), end="")
