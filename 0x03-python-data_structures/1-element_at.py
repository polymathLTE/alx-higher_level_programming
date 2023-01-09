#!/usr/bin/python3
# Author - Lawal Emmanuel

def element_at(my_list, idx):
    """ This function that retrieves an element from a list """
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
