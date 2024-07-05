#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()

        print(f"""Body response:
        \t- type: {type(content)}
        \t- content: {content}
        \t- utf8 content: {content.decode('utf-8')}""")
