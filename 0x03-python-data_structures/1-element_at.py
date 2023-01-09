#!/usr/bin/python3
# Author - Lawal Emmanuel

def element_at(my_list, idx):
    """ This function that retrieves an element from a list """
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]
