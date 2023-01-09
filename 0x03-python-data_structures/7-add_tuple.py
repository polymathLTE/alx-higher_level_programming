#!/usr/bin/python3
# Author - Lawal Emmanuel

def add_tuple(tuple_a=(), tuple_b=()):
    """ function that adds 2 tuples """
    # if len
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
print (len(new_tuple))
# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))
