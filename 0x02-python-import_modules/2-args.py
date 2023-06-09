#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

        for index, arg in enumerate(sys.argv, start=1):
                print("{}: {}".format(index, arg))
