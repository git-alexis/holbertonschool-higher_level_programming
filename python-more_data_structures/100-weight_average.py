#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    div = 0
    for number in my_list:
        sum += number[0] * number[1]
        div += number[1]
    return sum / div
