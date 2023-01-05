#!/usr/bin/python3

def print_last_digit(number):
    """
    function that prints the last digit of a number
    """
    ls_digit = int(abs(number) % 10)
    print("{}".format(ls_digit), end='')
    return ls_digit
