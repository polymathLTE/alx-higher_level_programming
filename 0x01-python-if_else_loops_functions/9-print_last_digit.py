#!/usr/bin/python3

def print_last_digit(number):
    """
    function that prints the last digit of a number
    """
    ls_digit = int(abs(number) % 10)
    if number < 0:
        ls_digit = ls_digit * -1
    print("{}".format(ls_digit))
