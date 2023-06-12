#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for i in range(len(my_string)):
        for c in my_string:
            if 'c' or 'C' in my_string:
                continue
            new_str += c
    return new_str
