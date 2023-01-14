#!/usr/bin/python3
# Author - Lawal Emmanuel

def weight_average(my_list=[]):
    """
    function that returns the weighted average of all integers tuple
    (<score>, <weight>)
    """
    val = 0
    if len(my_list) == 0:
        return 0
    for ls_i in range(len(my_list)):
        for tp_i in range(len(my_list[ls_i])):
            count = my_list[ls_i][tp_i] * my_list[ls_i][tp_i+1]
            break
        val += count
    val = val / 15
    return val
