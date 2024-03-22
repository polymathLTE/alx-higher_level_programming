#!/usr/bin/python3
# function that returns a set of all elements present in only set


def only_diff_elements(set_1, set_2):
    """
    """
    diff_elements = []
    diff_elements.extend([i for i in set_1 if i not in set_2])
    diff_elements.extend([i for i in set_2 if i not in set_1])
    return diff_elements
