#!/usr/bin/python3
#Author - Lawal Emmanuel

def remove_char_at(str, n):
    """
    function that creates a copy of the string, removing the character at the position n
    """
    if n >= len(str) or n < 0:
        return str
    return str.replace(str[n], "")

