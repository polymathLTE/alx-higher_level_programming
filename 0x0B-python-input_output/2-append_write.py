#!/usr/bin/python3
# Author - Lawal Emmanuel

def append_write(filename="", text=""):
    """appends a given text to file"""
    with open(filename, 'a', encoding='utf-8') as file_op:
        return file_op.write(text)
    
