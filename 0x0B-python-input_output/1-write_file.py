#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a write file function"""


def write_file(filename="", text=""):
    """writes a given text into specified file"""
    with open(filename, 'w', encoding='utf-8') as file_op:
        return file_op.write(text)
