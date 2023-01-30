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
        self._size = size

    @property
    def size(self):
        """ retrieves size of square
        Returns:
            _size: the set size of square
        """
        return (self._size)

    @size.setter
    def size(self, value):
        """ method to set the value of Square
        Args:
            value (int): new size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """ method that returns the current square area

        Returns:
            area: the computed area of Square.size
        """
        return (self._size * self._size)

    def my_print(self):
        """ that prints in stdout the square with the character # """
        if self._size == 0:
            print()
        for i in range(self._size):
            for j in range(self._size):
                print("#", end="")
            print()
