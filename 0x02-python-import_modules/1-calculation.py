#!/usr/bin/python3
# Author - Lawal Emmanuel

# prevents execution if imported
if __name__ == '__main__':
    # import required files
    from calculator_1 import add, sub, mul, div
    # init. variables
    a = 10
    b = 5

    # print using calc functions
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
