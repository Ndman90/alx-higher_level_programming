#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list,
    in reverse order"""
    list_length = len(my_list)
    index = list_length - 1

    for number in range(0, list_length):
        print("{:d}" .format(my_list[index]))
        index -= 1
