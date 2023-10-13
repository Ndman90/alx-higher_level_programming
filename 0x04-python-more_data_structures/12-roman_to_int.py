#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if roman_string is None or type(roman_string) is not str:
        return 0
    total = 0  """ To store the total integer value"""
    prev_value = 1000  """ To handle subtractive notation"""

    """ Dictionary to map Roman numerals to integers"""
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    """ Convert Roman numerals to integers and process them"""
    for numeral in roman_string:
        current_value = roman_dict.get(numeral, 0)
        if current_value > prev_value:
            total -= prev_value * 2
        prev_value = current_value
        total += current_value

    return (total)
