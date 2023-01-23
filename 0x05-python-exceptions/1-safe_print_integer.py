#!/usr/bin/python3
# Author - Lawal Emmanuel

def safe_print_integer(value):
    """
    function that prints an integer with "{:d}".format()
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
