#!/usr/bin/python3

"""
script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

Author - Lawal Emmanuel
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')

    req = urllib.request.Request(sys.argv[1], data=data)
    req.get_method = lambda: 'POST'

    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
