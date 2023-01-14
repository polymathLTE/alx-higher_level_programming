#!/usr/bin/python3
# Author - Lawal Emmanuel

def complex_delete(a_dictionary, value):
    """
    function that deletes keys with a specific value in a dictionary
    """
    if value not in a_dictionary.values():
        return a_dictionary
    indx = list(a_dictionary.values()).index(value)
    key = list(a_dictionary.keys())[indx]
    a_dictionary.pop(key)
    complex_delete(a_dictionary, value)
    return dict(a_dictionary)
