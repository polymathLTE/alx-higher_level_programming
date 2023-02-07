#!/usr/bin/python3
# Author - Lawal Emmanuel

def write_file(filename="", text=""):
    """writes a given text into specified file"""
    with open(filename, 'w') as file_op:
        file_op.write(text)
    return len(text)