#!/usr/bin/python3
# Author - Lawal Emmanuel
import json


def to_json_string(my_obj):
    """serializes given JSON-like object into string"""
    return json.dumps(my_obj, indent=1)
