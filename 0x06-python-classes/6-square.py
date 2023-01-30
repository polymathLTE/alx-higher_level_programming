#!/usr/bin/python3
# Author - Lawal Emmanuel


""" A class that defines square """


class Square:
    """ defines a square by attributes """
    def __init__(self, size=0, position=(0, 0)):
        """ this is instatiation code

        Args:
            size (int): given size of the square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrieves size of square
        Returns:
            _size: the set size of square
        """
        return (self._size)

    @size.setter
    def size(self, value):
        """ method to set the size of Square
        Args:
            value (int): new size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """ method to retrieve the position of Square """
        return (self._position)

    @position.setter
    def position(self, value):
        """ method to set the position of Square """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num > 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

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
            return
        [print("") for i in range(self._position[1])]
        for i in range(self._size):
            [print(' ', end="") for k in range(self._position[0])]
            [print("#", end="") for j in range(self._size)]
            print()
