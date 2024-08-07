#!/usr/bin/python3

"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Author - Lawal Emmanuel
"""

import requests
import sys

if __name__ == "__main__":

    payload = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        res = response.json()
        if len(res) == 0:
            print('No result')
        else:
            print(f"[{res.get('id')}] {res.get('name')}")

    except ValueError:
        print('Not a valid JSON')
