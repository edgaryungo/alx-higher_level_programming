#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        new_tuple = (tuple_a[0] + tuble_b[0], tuple_a[1] + tuble_b[1])
    if len(tuple_a) == 1 and len(tuple_b) == 2:
        new_tuple = (tuple_a[0] + tuple_b[0], 0 + tuble_b[1])
    if len(tuple_a) == 0 and len(tuple_b) == 2:
        new_tuple = (0 + tuble_b[0], 0 + tuble_b[1])
    if len(tuple_a) == 2 and len(tuple_b) == 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[0] + 0)
    if len(tuple_a) == 2 and len(tuple_b) == 0:
        new_tuple = (tuple_a[0] + 0, tuple_a[0] + 0)

    return new_tuple

