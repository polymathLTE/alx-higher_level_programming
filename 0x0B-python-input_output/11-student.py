#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a Student class"""


class Student:
    """represents a student object"""
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """initialization method for the student class

        Args:
            first_name (str): the first name of the student
            last_name (str): the lastname of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary repr of the student obj
        Args:
            attrs (list): (Optional) a list of attributes to be represented
        """
        if isinstance(attrs, list) and all(type(ele) == str for ele in attrs):
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)} 
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of a student instance

        Args:
            json (dict): its content replaces the attrs of the instance
        """
        for i in json.keys():
            if hasattr(self, i):
                self.i = json.get(i)
