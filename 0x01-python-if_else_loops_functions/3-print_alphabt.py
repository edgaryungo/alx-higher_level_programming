#!/usr/bin/python3
for ch in range(97, 123):
    if ch == 'q' or ch == 'e':
        continue
    else:
        print("{:c}".format(ch), end='')
