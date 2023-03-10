#!/usr/bin/python3
# Author - Lawal Emmanuel

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print("")
    except (TypeError, IndexError):
        print("")
    return count
