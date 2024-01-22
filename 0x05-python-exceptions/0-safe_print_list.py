#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    while x > 0:
        try:
            print("{}".format(my_list[printed]), end="")
            printed += 1
        except IndexError:
            pass
        x -= 1
    print()
    return printed
