from bisect import insort


"""This module supplies fast algorithms for pattern-related searches:
   longest palindrome, biggest elements in a list."""

def find_n_biggest_numbers(numbers, amount=20):
    """return the nth biggest elements in the list"""
    if len(numbers) > amount:
        biggest_numbers = sorted(numbers[:amount])
    else:
        return numbers


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
        check_even = False
        for _ in range(2):
            current_length = _palindrome_length(base_string, index, check_even)
            if current_length > longest_length:
                longest_length = current_length
                start_index = index
            check_even = not check_even
    
    
    return _rebuild_palindrome(base_string, start_index, longest_length)


def _palindrome_length(base_string, middle, check_even=False):
    function_offset = 0
    if check_even:
        function_offset = 1

    distance_from_middle = 1
    right = distance_from_middle + middle + function_offset
    left = middle - distance_from_middle

    while right < len(base_string) and left >= 0 and base_string[right] == base_string[left]:
        distance_from_middle += 1
        right = distance_from_middle + middle + function_offset
        left = middle - distance_from_middle

    if not check_even:
        return (distance_from_middle * 2) - 1
    return (distance_from_middle * 2) - 1 + function_offset


def _rebuild_palindrome(base_string, start_index, length):
    begining = start_index - int(length/2)
    if length % 2 == 0:
        begining += 1
    end = start_index + int(length / 2) + 1
    return base_string[begining:end]