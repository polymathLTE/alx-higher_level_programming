#!/usr/bin/python3
# Author - Lawal Emmanuel

def uniq_add(my_list=[]):
    """
    function that adds all unique integers in a list
    (only once for each integer)
    """
    count = 0
    count_lst = []
    for i in my_list:
        if i not in count_lst:
            count += i
            count_lst.append(i)
    return count
