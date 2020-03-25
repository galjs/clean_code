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
    longest_palindrome_length = 0
    longest_palindrome_start_index = 0

    for index in range(len(base_string) - 1):
        current_length = _palindrome_length(base_string, index)
        if current_length > longest_palindrome_length:
            longest_palindrome_length = current_length
            longest_palindrome_start_index = index
    
    begining = longest_palindrome_start_index - int(longest_palindrome_length/2)
    end = longest_palindrome_start_index + int(longest_palindrome_length / 2) + 1

    if not longest_palindrome_length % 2 == 0:
        return base_string[begining:end]
    else:
        return base_string[begining + 1:end]


def _palindrome_length(base_string, middle, check_even=False):
    function_offset = 0
    if check_even:
        function_offset = 1

    distance_from_middle = 1
    while distance_from_middle + middle + function_offset < len(base_string) and middle - distance_from_middle >= 0:
        if base_string[middle + function_offset + distance_from_middle] == base_string[middle - distance_from_middle]:
            distance_from_middle += 1
        else:
            break
    if not check_even:
        return max(_palindrome_length(base_string, middle, True), (distance_from_middle * 2) - 1 + function_offset)
    return (distance_from_middle * 2) - 1 + function_offset