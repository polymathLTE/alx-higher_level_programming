#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    response = requests.post(url=sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
