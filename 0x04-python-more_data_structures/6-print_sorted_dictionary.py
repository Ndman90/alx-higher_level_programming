#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    if a_dictionary is None:
        return
    for keys in sorted(a_dictionary.keys()):
        print('{}: {}'. format(keys, a_dictionary[keys]))
