#!/usr/bin/python3
# Author - Lawal Emmanuel

def update_dictionary(a_dictionary, key, value):
    """
    function that replaces or adds key/value in a dictionary
    """
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary.update(key, value)
