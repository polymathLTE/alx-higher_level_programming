#!/usr/bin/python3
# Author - Lawal Emmanuel

def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values multiplied by 2
    """
    new_dict = {}
    for i in a_dictionary.keys():
        temp_dict = {i: a_dictionary.get(i) * 2}
        new_dict.update(temp_dict)
    return new_dict
