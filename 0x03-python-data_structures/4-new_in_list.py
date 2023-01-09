#!/usr/bin/python3
# Author - Lawal Emmanuel

def new_in_list(my_list, idx, element):
    """
    function that replaces an element in a list at a specific position
    without modifying the original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        list_cpy = my_list.copy()
        list_cpy[idx] = element
    return list_cpy
