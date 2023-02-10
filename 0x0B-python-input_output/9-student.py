#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a Student class"""


class Student:
    """represents a student object"""
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """initialization method for the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary repr of the student obj"""
        return self.__dict__
