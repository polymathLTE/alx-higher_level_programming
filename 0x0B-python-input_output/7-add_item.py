#!/usr/bin/python3
# Author - Lawal Emmanuel

# import libraries
import sys
import json
from os import path as pt
# import needed functions
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

f_content = []

# checks if file exists
if not pt.exists('./add_item.json'):
    save_json(f_content, 'add_item.json')

# appends the given arguments if present
if len(sys.argv) > 1:
    f_content = load_json('add_item.json')
    for i in range(len(sys.argv) - 1):
        f_content.append(sys.argv[i+1])
    save_json(f_content, 'add_item.json')
