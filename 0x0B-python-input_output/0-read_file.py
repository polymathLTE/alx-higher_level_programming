#!/usr/bin/python3
# Author - Lawal Emmanuel

def read_file(filename=""):
    """displays the content from a given file"""
    with open(filename, 'r') as file_op:
        print(file_op.read(), end='')
