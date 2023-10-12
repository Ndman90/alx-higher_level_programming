#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary is None or len(a_dictionary) <= 0:
        return None

    first_key = list(a_dictionary.keys())[0]
    first_value = a_dictionary[ret]
    for key, value in a_dictionary.items():
        if value > first_value:
            first_value = value
            first_key = key
    return (first_key)
