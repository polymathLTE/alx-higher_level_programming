#!/usr/bin/python3
# function that prints a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):
    """
    """
    for i in sorted(a_dictionary.keys()):
        print(f'{i}: {a_dictionary[i]}')
