#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a function that loads a json obj form file"""


import json


def load_from_json_file(filename):
    """load and return content from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
