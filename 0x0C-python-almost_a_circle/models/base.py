#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a base class"""


class Base:
    """base class of all projec tasks"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base class constructor/initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
