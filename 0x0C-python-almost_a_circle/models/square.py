#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square which inherits the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square class constructor/init function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of square"""
        self.width = value
        self.height = value        

    def __str__(self):
        """returns a readable representation of the Square. class
        Return:
            [Square] (<id>) <x>/<y> - <size>
        """
        msg = "Square ({}) {}/{} - {}"
        return msg.format(self.id, self.x,
                          self.y, self.width)
