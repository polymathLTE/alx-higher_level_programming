#!/usr/bin/python3
# Author - Lawal Emmanuel

import sys


def safe_function(fct, *args):
    """
    function that executes a function safely
    """
    try:
        ret = fct(*args)
        return ret
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return 'None'
