#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body of the response
displays Error code if >400

Author - Lawal Emmanuel
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
