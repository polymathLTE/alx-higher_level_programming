#!/usr/bin/python3.4
# Author - Lawal Emmanuel

def multiple_returns(sentence):
    """
    function that returns a tuple with the length of a string
    and its first character
    """
    if len(sentence) == 0:
        sentence_info = (len(sentence), 'None')
        return sentence_info
    else:
        sentence_info = (len(sentence), sentence[0])
        return sentence_info
