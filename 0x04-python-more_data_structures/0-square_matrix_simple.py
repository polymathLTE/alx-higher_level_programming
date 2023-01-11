#!/usr/bin/python3
# Author - Lawal Emmanuel

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix
    """
    new_matrix = []
    square = lambda n: n*n
    new_matrix = list(map(lambda row : list(map(square, row)), matrix))
    return new_matrix
