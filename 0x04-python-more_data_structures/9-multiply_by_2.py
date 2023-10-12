#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    if a_dictionary is None:
        return None
    dict_copy = {}
    for key, value in a_dictionary.items():
        dict_copy[key] = value * 2
    return dict_copy
