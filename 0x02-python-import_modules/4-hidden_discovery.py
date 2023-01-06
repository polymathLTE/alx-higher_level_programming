#!/usr/bin/python3
# Author - Lawal Emmanuel

if __name__ == '__main__':

    import hidden_4

    lst = sorted(dir(hidden_4))
    for i in len(lst):
        if not lst[i].startswith('__'):
            print("{}".format(lst[i]))
