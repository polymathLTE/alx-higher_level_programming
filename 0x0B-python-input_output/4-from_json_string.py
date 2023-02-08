#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a string to json function"""


import json


def from_json_string(my_str):
    """
    Deserialize obj as (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
