#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_reversed_list_integer(my_list=[]):
    """ function that prints all integers of a list, in reverse order """
    my_list.reverse()
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
