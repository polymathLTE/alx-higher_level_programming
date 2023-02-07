#!/usr/bin/python3
# Author - Lawal Emmanuel

def append_write(filename="", text=""):
    """appends a given text to file"""
    with open(filename, 'a') as file_op:
        file_op.write(text)
    return len(text)