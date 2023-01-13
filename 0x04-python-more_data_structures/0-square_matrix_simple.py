#!/usr/bin/python3
# Author - Lawal Emmanuel

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix
    """
    new_matrix = []

    def square(num):
        num = num * num
        return num

    new_matrix = list(map(lambda row: list(map(square, row)), matrix))
    return new_matrix
