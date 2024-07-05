#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    request_id = response.headers.get('X-Request-Id')
    print(request_id)
