#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys

data = urllib.parse.urlencode({'email': sys.argv[2]})
data = data.encode('ascii')

req = urllib.request.Request(sys.argv[1], data=data) 
req.get_method = lambda: 'POST'

with urllib.request.urlopen(req) as f:
  print(f.read().decode('utf-8'))
