#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args_num = len(sys.argv) - 1

    if args_num == 0:
        print("{} arguments." .format(args_num))
    elif args_num == 1:
        print("{} argument:" .format(args_num))
        print("{}: {}" .format(args_num, sys.argv[args_num]))
    else:
        print("{} arguments:" .format(args_num))
        count = 1
        for args in range(1, (args_num + 1)):
            print("{}: {}" .format(count, sys.argv[args]))
            count += 1
