#!/usr/bin/python3
for ch in range(97, 123):
    if ch is 'q' or ch is 'e':
        continue
    else:
        print("{:c}".format(ch), end='')
