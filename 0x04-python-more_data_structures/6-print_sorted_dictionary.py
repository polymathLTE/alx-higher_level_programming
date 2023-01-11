#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys
    """
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
