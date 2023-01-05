#!/usr/bin/python3
# Author - Lawal Emmanuel

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0 #switch state of i to alternate upper and lowercase
