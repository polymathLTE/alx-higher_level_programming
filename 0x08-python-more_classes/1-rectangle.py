#!/usr/bin/python3
# Author - Lawal Emmanuel

""" This defines a rectangle class """


class Rectangle:
    """ simple implementation of a rectangle """
    def __init__(self, width=0, height=0):
        """this initializes an object on creation
        Args:
            width (int): the init width of rectangle obj
            height (int): the init height of rectangle obj
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of the rectangle obj"""
        return self._width

    @width.setter
    def width(self, value):
        """sets the width if the rectangle obj
        Args:
            value (int): the setter value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """retrieves the height of the rectangle obj"""
        return self._height

    @height.setter
    def height(self, value):
        """sets the height if the rectangle obj
        Args:
            value (int): the setter value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
