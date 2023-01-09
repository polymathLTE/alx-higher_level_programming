#!/usr/bin/python3
# Author - Lawal Emmanuel

def delete_at(my_list=[], idx=0):
    """
    function that deletes the item at a specific position in a list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
    return my_list
