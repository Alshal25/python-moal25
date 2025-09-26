#!/usr/bin/env python3

import random
from marvin1 import calculate_luhna_sum

def create_ssn(birth_date):
    digit1 = random.randint(0, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)

    partial_ssn = birth_date + str(digit1) + str(digit2) + str(digit3)
    luhn_sum = calculate_luhna_sum(partial_ssn)
    last_digit = (10 - (luhn_sum % 10)) % 10
    complete_ssn = birth_date + "-" + str(digit1) + str(digit2) + str(digit3) + str(last_digit)
    return complete_ssn

def randomize_string(input_string):
    if len(input_string) <= 1:
        return input_string

    result = ""
    temp_string = input_string

    while temp_string:
        random_index = random.randint(0, len(temp_string) - 1)
        result = result + temp_string[random_index]
        temp_string = temp_string[:random_index] + temp_string[random_index + 1:]
    return result

def find_all_indexes(main_string, substring):
    if not substring:
        return ""

    indexes = ""
    start_pos = 0

    while True:
        try:
            index = main_string.index(substring, start_pos)
            if indexes:
                indexes = indexes + "," + str(index)
            else:
                indexes = str(index)
            start_pos = index + 1
        except ValueError:
            break
    return indexes
