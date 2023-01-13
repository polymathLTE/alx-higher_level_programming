#!/usr/bin/python3
# Author - Lawal Emmanuel

def simple_delete(a_dictionary, key=""):
    """
    function that deletes a key in a dictionary
    """
    if len(key) == 0:
        return a_dictionary
    elif key not in a_dictionary.keys():
        return a_dictionary
    else:
        a_dictionary.pop(key)
        return a_dictionary
