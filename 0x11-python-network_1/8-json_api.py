#!/usr/bin/python3

import requests
import sys

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

