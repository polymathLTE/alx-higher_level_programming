#!/usr/bin/python3
# Author - Lawal Emmanuel

def read_file(filename=""):
    """displays content from a given file"""
    with open(str(filename), 'r') as op_file:
        print(op_file.read())
