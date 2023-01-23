#!/usr/bin/python3
# Author - Lawal Emmanuel

def safe_print_division(a, b):
    """
    function that divides 2 integers and prints the result
    """
    ret = 'None'
    try:
        ret = a / b
    except ValueError:
        return ret
    finally:
        print("Inside result: {}".format(ret))
        return ret
