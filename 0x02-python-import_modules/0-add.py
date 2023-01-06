#!/usr/bin/python3
# Author - Lawal Emmanuel

# import test files
# import sys
# sys.path.append("./test_files")

# import required modules
from add_0 import add

# block execution if imported
if __name__ == '__main__':
    # init. variables
    a = 1
    b = 2

    # display format = <a value> + <b value> = <add(a, b) value>
    print("{} + {} = {}".format(a, b, add(a, b)))
