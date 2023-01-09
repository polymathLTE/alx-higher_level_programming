#!/usr/bin/python3
# Author - Lawal Emmanuel

def max_integer(my_list=[]):
    """ function that finds the biggest integer of a list """
    if len(my_list) == 0:
        return 'None'
    my_list.sort()
    maxx = my_list[-1]
    return maxx
