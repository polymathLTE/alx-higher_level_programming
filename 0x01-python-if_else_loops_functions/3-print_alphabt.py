#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_lowerAlpha():
    '''
    function to print the ASCII alphabet in lowercase
    not followed by new line
    '''
    for c in range(97, 122):
        if c == 101 or c == 113:
            continue
        else:
            print(chr(c), end="")


print_lowerAlpha()
