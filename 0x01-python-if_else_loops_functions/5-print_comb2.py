#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_num_rng(start, stop):
    '''
    function to print numbers in given range
    '''
    for i in range(start, stop+1):
        if i == stop:
            print("{}".format(i))
        else:
            print("{0:0=2d},".format(i), end=' ')


print_num_rng(0, 99)
