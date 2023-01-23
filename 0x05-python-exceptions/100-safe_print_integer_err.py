#!/usr/bin/python3
# Author - Lawal Emmanuel

import sys


def safe_print_integer_err(value):
    """
    function that prints an integer
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
