#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """this class inherits the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square class constructor/init function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a readable representation of the Square. class
        Return:
            [Square] (<id>) <x>/<y> - <width>/<height>
        """
        msg = "Square ({}) {}/{} - {}/{}"
        return msg.format(self.id, self.x,
                          self.y, self.width, self.height)
