#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.getheaders()

        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
