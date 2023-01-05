#!/usr/bin/python3

'''
function to print the ASCII alphabet in lowercase not followed by new line
'''
def print_lowerAlpha():
    for c in range(97, 122):
        print(chr(c), end="")

print_lowerAlpha()
