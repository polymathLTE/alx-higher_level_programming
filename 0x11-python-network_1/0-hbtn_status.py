#!/usr/bin/python3

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()

print(f"""Body response:
\t- type: {type(content)}
\t- content: {content}
\t- utf8 content: {content.decode('utf-8')}""")
