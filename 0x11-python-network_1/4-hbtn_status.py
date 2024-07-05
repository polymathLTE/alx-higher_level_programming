#!/usr/bin/python3

import requests

data = requests.get('https://alx-intranet.hbtn.io/status')


print(f"""Body response:
\t- type: {type(data.text)}
\t- content: {data.text}""")
