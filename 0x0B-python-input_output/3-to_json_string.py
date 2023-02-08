#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a json to string function"""


import json


def to_json_string(my_obj):
    """serializes given JSON-like object into string"""
    return json.dumps(my_obj)
