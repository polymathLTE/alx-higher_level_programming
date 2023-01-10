#!/usr/bin/python3
# Author - Lawal Emmanuel

def print_matrix_integer(matrix=[[]]):
    """ This function that prints a matrix of integers """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end="" if j+1 == len(matrix[0]) else " ")
        print()
