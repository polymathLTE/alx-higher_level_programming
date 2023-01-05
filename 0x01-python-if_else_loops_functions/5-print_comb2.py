#!/usr/bin/python3

'''
function to print numbers in given range
'''

def print_num_rng(start, stop):
    for i in range(start, stop+1):
        if i == stop:
            print(i)
        else:
            print("{0:0=2d},".format(i), end=' ')

print_num_rng(0, 99)
