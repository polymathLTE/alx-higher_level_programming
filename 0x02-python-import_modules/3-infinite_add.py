#!/usr/bin/python3

# run only as script/ not if imported
if __name__ == '__main__':

    # import modules
    import sys

    # init variables
    ret_int = 0
    sysa = sys.argv

    for i in range(len(sysa) - 1):
        ret_int = int(ret_int) + int(sysa[i+1])
    print(ret_int)
