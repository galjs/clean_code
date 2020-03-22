

def sum_arithmetic_progress(difference, first_element, number_of_elements):
    total = (number_of_elements * (2 * first_element + difference * (number_of_elements - 1))) / 2
    return total


def find_missing_number(numbers):
    arithmetic_sum = sum_arithmetic_progress(1, 0, len(numbers) + 1)
    sum_of_numbers = sum(numbers)

    return int(arithmetic_sum - sum_of_numbers)