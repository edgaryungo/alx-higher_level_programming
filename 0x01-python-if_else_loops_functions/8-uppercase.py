#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            cap = 32
        else:
            cap = 0
        print("{:c}".format(ord(str[i]) - cap), end='')
    print()
