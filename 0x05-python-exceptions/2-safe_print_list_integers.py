#!/usr/bin/python3
# Author - Lawal Emmanuel

def safe_print_list_integers(my_list=[], x=0):
    """
    function that prints the first x elements of a list and only integers
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except(TypeError, ValueError):
            pass
    print()
    return count
