#!/usr/bin/python3
# Author - Lawal Emmanuel

def read_file(filename=""):
    """displays the content from a given file"""
    with open(filename, 'r', encoding='utf-8') as file_op:
        print(file_op.read(), end='')
