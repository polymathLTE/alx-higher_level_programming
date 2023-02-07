#!/usr/bin/python3
# Author - Lawal Emmanuel

import json
def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    obj_str = eval(obj.str())
    return dict(json.loads(obj_str))
    
