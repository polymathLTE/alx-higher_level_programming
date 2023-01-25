#!/usr/bin/python3
# Author - Lawal Emmanuel

""" A class that defines square """


class Square:
    """ defines a square by attributes """
    def __init__(self, size):
        """ this is instatiation code

        Args:
            size: given size of the square

        """
        if size is not None:
            self._size = size
