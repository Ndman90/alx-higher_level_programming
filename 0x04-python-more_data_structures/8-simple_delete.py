#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""
    if a_dictionary is None or key is None:
        return
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
