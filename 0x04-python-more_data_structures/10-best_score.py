#!/usr/bin/python3
# function that returns a key with the biggest integer value


def best_score(a_dictionary):
    """
    """
    big_score = 0
    largest = ''
    if type(a_dictionary) != dict:
        return None

    for i in a_dictionary.keys():
        if a_dictionary[i] > big_score:
            largest = i
        else:
            return None
    return largest
