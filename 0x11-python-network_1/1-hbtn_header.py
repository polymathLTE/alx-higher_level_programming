#!/usr/bin/python3

"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response

Author - Lawal Emmanuel
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.getheaders()

        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
