#!/usr/bin/python3

def no_c(my_string):
    modified_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            modified_str += char
    return (modified_str)
