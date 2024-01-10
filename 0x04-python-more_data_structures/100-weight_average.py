#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = sum((i[0] * i[1]) for i in my_list)
    den = sum(i[1] for i in my_list)

    return num / den
