#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))
        for index in range(1, len(argv)):
            print("{}: {}".format(index, argv[index]))
