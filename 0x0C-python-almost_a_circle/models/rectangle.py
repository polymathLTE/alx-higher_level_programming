#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a rectangle class that inherits from base"""

from models.base import Base


class Rectangle(Base):
    """this defines the properties of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle class constructor/init function"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter: this returns the width size"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter: sets the value of width
        Args:
            value (int): the new value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter: this returns the height size"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter: sets the value of height
        Args:
            value (int): the new height to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter: this returns the x position"""
        return self.__x

    @height.setter
    def x(self, value):
        """x setter: sets the value of x
        Args:
            value (int): the new x to be set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """x getter: this returns the x position"""
        return self.__y

    @height.setter
    def y(self, value):
        """y setter: sets the value of y
        Args:
            value (int): the new y to be set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of the Rect. obj."""
        return self.width * self.height

    def display(self):
        """displays the size of Rect. obj. using '# """
        [print() for i in range(self.__y) if self.__y > 0]
        for i in range(self.height):
            [print(' ', end="") for k in range(self.x) if self.__x > 0]
            [print('#', end="") for j in range(self.width)]
            print()

    def __str__(self):
        """returns a readable representation of the Rect. class
        Return:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        msg = "Rectangle ({}) {}/{} - {}/{}"
        return msg.format(self.id, self.__x,
                          self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """this updates the class by singular attr. or a dictionary
        of attrs
        Args:
            args (list): list of attributes to be updated
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            kwargs (dict): dictionary of items to be updated
        """
        if len(args) > 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1
        elif len(args) == 0 and len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
