#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_dec_hex(start, stop):
    '''
    function that prints numbers in given range,
    in both dec. and hex. formats
    '''
    for i in range(start, stop+1):
        print("{} = {}".format(i, hex(i)))


print_dec_hex(0, 98)
