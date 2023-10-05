#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if ord('q') is not char and ord('e') is not char:
        print("{}".format(chr(char)), end='')
