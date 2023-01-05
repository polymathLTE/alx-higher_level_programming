#!/usr/bin/python3

'''
function that prints numbers in given range in both dec. and hex. formats
'''

def print_dec_hex(start, stop):
    for i in range(start, stop+1):
        print("{} = {}".format(i, hex(i)))

print_dec_hex(0, 98)
