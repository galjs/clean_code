
"""Recieves a list of consecutive numbers when only one is missing.
   returns the missing number."""

def sum_arithmetic_progress(number_of_elements, difference=1, first_element=0):
    total = (number_of_elements * (2 * first_element + difference * (number_of_elements - 1))) / 2
    return total


def find_missing_number(numbers):
    arithmetic_progress_sum = sum_arithmetic_progress(len(numbers)+1)
    numbers_sum = sum(numbers)
    return int(arithmetic_progress_sum - numbers_sum)