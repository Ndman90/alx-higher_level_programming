#!/usr/bin/python3

if __name__ == "__main__":
    """Add and print all arguments."""
    import sys

    args_num = len(sys.argv)
    sum = 0
    for args in range(1, args_num):
        sum += int(sys.argv[args])
    print("{}" .format(sum))
