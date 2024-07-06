#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status

it uses the 'requests' package
Author - Lawal Emmanuel
"""

import requests

if __name__ == "__main__":
    data = requests.get('https://alx-intranet.hbtn.io/status')

    print(f"""Body response:
    \t- type: {type(data.text)}
    \t- content: {data.text}""")
