#!/usr/bin/python3
# Author - Lawal Emmanuel

""" A class that defines square """


class Square:
    """ defines a square by attributes """
    def __init__(self, size=0):
        """ this is instatiation code

        Args:
            size (int): given size of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """ method that returns the current square area

        Returns:
            area: the computed area of Square.size
        """
        return (self._size * self._size)
