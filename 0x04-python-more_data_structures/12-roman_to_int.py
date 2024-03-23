#!/usr/bin/python3
# Author - Lawal Emmanuel


def roman_to_int(roman_string):
    """
    """
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    num = 0
    for idx, i in enumerate(roman_string):
        if idx > 0 and roman_numerals[roman_string[idx-1]] < roman_numerals[i]:
            num += roman_numerals[i] - roman_numerals[roman_string[idx-1]] *2
        else:
            num += roman_numerals[i]

    return num
