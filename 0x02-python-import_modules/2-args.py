#!/usr/bin/python3
# Author - Lawal Emmanuel

# run only as script/ not if imported
if __name__ == '__main__':
    # import modules
    import sys as sy

    # init variable
    sysa = sy.argv
    gramr_num = "arguments"
    gramr_sufx = ":"

    # print the number of the argument
    if len(sysa) == 2:
        gramr_num = "argument"
    if len(sysa) == 1:
        gramr_sufx = "."
    print("{} {}{}".format(len(sysa) - 1, gramr_num, gramr_sufx))

    # print the values of the argument
    for i in range(len(sysa) - 1):
        print("{}{} {}".format(i+1, gramr_sufx, sysa[i+1]))
