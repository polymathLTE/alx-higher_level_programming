#!/usr/bin/python3

"""
script that sends a POST request and prints the response
it uses the requests library

Author - Lawal Emmanuel
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.post(url=sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
