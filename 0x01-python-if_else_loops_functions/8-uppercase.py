#!/usr/bin/python3
# Author - Lawal Emmanuel

def uppercase(str):
    """
    function that prints a string in uppercase followed by a new line
    """
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:  # checks if lowercase
            i = chr(ord(i) - 32)  # converts to uppercase
        print("{}".format(i), end='')
    print("{}".format(''))
