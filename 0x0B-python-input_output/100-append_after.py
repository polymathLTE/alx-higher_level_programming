#!/usr/bin/python3
# Author - Lawal Emmanuel

"""Defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string
    Args:
        filename (string): the file to be written into
        search_string (string): the string to be searched for
        new_string (string): the string to be inserted
    """
    f_write = []
    with open(filename, 'r+', encoding='utf-8') as f:
        f_content = f.readlines()
        for rd_line in f_content:
            f_write.append(rd_line)
            if search_string in rd_line:
                f_write.append(new_string)
        f.write("")

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(f_write)
