#!/usr/bin/python3
# Author - Lawal Emmanuel

""" This defines a rectangle class """


class Rectangle:
    """ simple implementation of a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """this initializes an object on creation
        Args:
            width (int): the init width of rectangle obj
            height (int): the init height of rectangle obj
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calc. and returns the area of the rec. obj
        Returns:
            The area of the rect. obj.
        """
        return (self._width * self._height)

    def perimeter(self):
        """calc. and return the perimeter of the rec. obj
        Returns:
            the perimeter of the rect. obj
        """
        if self._width == 0 or self.height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """computes and displays the size of the rect. obj using
        Returns:
            displays a size representation of rect obj using '#
        """
        apv = []
        wid = self._width
        hgt = self._height
        if wid == 0 or hgt == 0:
            return ""
        for i in range(hgt):
            [apv.append(str(self.print_symbol)) for j in range(wid)]
            if i != hgt - 1:
                apv.append('\n')
        return "".join(apv)

    def __repr__(self):
        """returns a canonical representation of the rect. obj;
        a curated string that can be used by eval
        Returns:
            curated f-string
        """
        return ("Rectangle({}, {})".format(self._width, self._height))

    def __del__(self):
        """destructor - deletes an instance of rect. obj."""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
