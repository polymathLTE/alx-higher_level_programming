#!/usr/bin/python3
# Author - Lawal Emmanuel

def best_score(a_dictionary):
    """function that returns a key with the biggest integer value"""
    if a_dictionary is None:
        return 'None'
    max_score = max(a_dictionary.values())
    best = list(a_dictionary.values()).index(max_score)
    return list(a_dictionary.keys())[best]
