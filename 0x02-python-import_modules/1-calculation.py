#!/usr/bin/python3
# Author - Lawal Emmanuel

# import test files
# import sys
# sys.path.append("./test_files")

# import required files
import calculator_1 as calc

# prevents execution if imported
if __name__ == '__main__':
    # init. variables
    a = 10
    b = 5

    # print using calc functions
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
