#!/usr/bin/python3
# function that deletes a key in a dictionary.


def simple_delete(a_dictionary, key=""):
    """
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
