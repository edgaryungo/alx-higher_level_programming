#!/usr/bin/python3
def no_c(my_string):
    remove = ['c', 'C']

    s = "".join(c for c in my_string if c not in remove)
    return s.strip()
