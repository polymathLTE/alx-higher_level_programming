#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_matrix_integer(matrix=[[]]):
    """ This function that prints a matrix of integers """
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end="" if j == i[-1] else " ")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
