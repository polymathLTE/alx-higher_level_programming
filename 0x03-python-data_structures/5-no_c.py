#!/usr/bin/python3
# Author - Lawal Emmanuel

def no_c(my_string):
    """function that removes all characters c and C from a string """
    ret_string = ''
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            ret_string += my_string[i]
    return ret_string
