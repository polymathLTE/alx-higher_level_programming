#!/usr/bin/python3

"""
script that fetches https://alx-intranet.hbtn.io/status

Author - Lawal Emmanuel
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()

        print(f"""Body response:
        - type: {type(content)}
        - content: {content}
        - utf8 content: {content.decode('utf-8')}""")
