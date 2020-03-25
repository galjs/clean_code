
from collections import Counter
from math import factorial
from bisect import insort

"""This module supplies fast algorithms for pattern-related searches."""

def find_n_biggest_numbers(numbers, amount=20):
    if len(numbers) > amount:
        biggest_numbers = sorted(numbers[:amount])
    else:
        return numbers


    for number in numbers:
        if number > biggest_numbers[0]:
            insort(biggest_numbers, number)
            del biggest_numbers[0]

    return biggest_numbers


def create_trimmed_string(base_string):
    return ''.join(base_string[index] for index in range(1, len(base_string)) if base_string[index] != base_string[index-1])


def find_longest_palindrome(base_string):
    longest_pali_length = 0
    longest_pali_start_index = 0
    is_odd = True

    for index in range(len(base_string) - 1):
        current_length = _odd_palindrome_length(base_string, index)
        if current_length > longest_pali_length:
            longest_pali_length = current_length
            longest_pali_start_index = index
            is_odd = True

        if current_length == 1 and base_string[index] == base_string[index+1]:
            current_length = _even_palindrome_length(base_string, index, index+1)
            if current_length > longest_pali_length:
                longest_pali_length = current_length
                longest_pali_start_index = index
                is_odd = False
    
    begining = longest_pali_start_index - int(longest_pali_length/2)
    end = longest_pali_start_index + int(longest_pali_length / 2) + 1

    if is_odd:
        return base_string[begining:end]
    else:
        return base_string[begining + 1:end]


def _odd_palindrome_length(base_string, middle):
    pali_length = 1
    distance_from_middle = 1
    while distance_from_middle + middle < len(base_string) and middle >= distance_from_middle:
        if base_string[middle + distance_from_middle] == base_string[middle - distance_from_middle]:
            pali_length += 2
            distance_from_middle += 1
        else:
            return pali_length

    return pali_length


def _even_palindrome_length(base_string, middle_left, middle_right):
    pali_length = 2
    distance_from_middle = 1
    while distance_from_middle + middle_right < len(base_string) and middle_left >= distance_from_middle:
        if base_string[middle_right + distance_from_middle] == base_string[middle_left - distance_from_middle]:
            pali_length += 2
            distance_from_middle += 1
        else:
            return pali_length

    return pali_length


def generate_permutations_iterably(elements):
    permutations = []
    expectd_permutations_number = factorial(len(elements))

    new_permutations = _generate_new_permutations(elements)
    permutations.extend(filter(lambda item: item not in permutations, new_permutations))
    
    while len(permutations) < expectd_permutations_number:
        permutations_copy = list(permutations)

        for permutation in permutations_copy:
            new_permutations = _generate_new_permutations(permutation)
            permutations.extend(filter(lambda item: item not in permutations, new_permutations))
    
    return [''.join(permutation) for permutation in permutations]


def _generate_new_permutations(base_state):
    new_permutations = []
    for index in range(len(base_state)):
        base_state_copy = list(base_state)
        base_state_copy[0], base_state_copy[index] = base_state_copy[index], base_state_copy[0]
        new_permutations.append(base_state_copy)

    return new_permutations


def generate_permutations_recursively(base_string):
    return list(_generate_permutations_recursively(list(base_string)))


def _generate_permutations_recursively(elements):
    permutations = []
    if len(elements) == 1:
        return [elements[0]]

    for index in range(len(elements)):
        elements_copy = list(elements)
        elements_copy[0], elements_copy[index] = elements_copy[index], elements_copy[0]
        for combination in _generate_permutations_recursively(elements_copy[1:]):
            new_permutation = elements_copy[0] + ''.join(combination)
            permutations.append(new_permutation)

    return permutations