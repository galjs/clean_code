from bisect import insort


"""This module supplies fast algorithms for pattern-related searches:
   longest palindrome, biggest elements in a list."""

def find_n_biggest_numbers(numbers, amount=20):
    """return the nth biggest elements in the list"""
    if len(numbers) <= amount:
        return numbers
    biggest_numbers = sorted(numbers[:amount])

    for number in numbers:
        if number > biggest_numbers[0]:
            insort(biggest_numbers, number)
            del biggest_numbers[0]

    return biggest_numbers


def find_longest_palindrome(base_string):
    """returns the longest palindrome in a string"""
    longest_length = 0
    start_index = 0

    for index in range(len(base_string) - 1):
        for check_even in [True, False]:
            current_length = _palindrome_length(base_string, index, check_even)
            longest_length, start_index = max((longest_length, start_index), (current_length, index))
    
    
    return _rebuild_palindrome(base_string, start_index, longest_length)


def _palindrome_length(base_string, middle, check_even):
    function_offset = 1 if check_even else 0

    distance_from_middle = 1
    right_end = distance_from_middle + middle + function_offset
    left_end = middle - distance_from_middle

    while right_end < len(base_string) and left_end >= 0 and base_string[right_end] == base_string[left_end]:
        distance_from_middle += 1
        right_end = distance_from_middle + middle + function_offset
        left_end = middle - distance_from_middle

    if not check_even:
        return (distance_from_middle * 2) - 1
    return (distance_from_middle * 2)


def _rebuild_palindrome(base_string, start_index, length):
    begining = start_index - int(length/2)
    if length % 2 == 0:
        begining += 1
    end = start_index + int(length / 2) + 1
    return base_string[begining:end]