#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ids = sort(a_dictionary.keys())
    for i in ids:
        print("{}: {}".format(i, a_dictionary.get(i)))
