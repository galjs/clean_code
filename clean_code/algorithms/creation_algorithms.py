from math import factorial

"""This module supplies fast algorithms for pattern-related creations:
   all permutations of a staring, duplicate-deletion."""

def create_trimmed_string(base_string):
    """deletes duplicates in a string. example: aaabbaac -> abac"""
    trimmed_elements = [base_string[0]]
    for index in range(1, len(base_string)):
        if base_string[index] != base_string[index-1]:
            trimmed_elements.append(base_string[index])
    return ''.join(trimmed_elements)


def generate_permutations_iterably(elements):
    """returns all the permutations of a string. the function is non-recursive"""
    permutations = set()
    final_permutations = set()
    next_index_to_be_permutated = 0
    expectd_permutations_number = factorial(len(elements))

    new_permutations = _generate_new_permutations(elements)
    permutations.update(new_permutations)

    while len(permutations) < expectd_permutations_number:
        permutations_copy = permutations.copy()
        permutations = set()

        for permutation in permutations_copy:
            new_permutations = _generate_new_permutations(permutation)
            final_permutations.update(new_permutations)
            permutations.update(new_permutations)

    return [''.join(permutation) for permutation in final_permutations]


def _generate_new_permutations(base_state):
    new_permutations = []
    for index in range(len(base_state)):
        base_state_copy = list(base_state)
        _switch_cells(base_state_copy, 0, index)
        new_permutations.append(base_state_copy)

    return [''.join(permutation) for permutation in new_permutations]


def generate_permutations_recursively(base_string):
    """returns all the permutations of a string. the function is recursive"""
    return _generate_permutations_recursively(list(base_string))


def _generate_permutations_recursively(elements):
    permutations = []
    if len(elements) == 1:
        return elements

    for index in range(len(elements)):
        elements_copy = list(elements)
        _switch_cells(elements_copy, 0, index)
        for combination in _generate_permutations_recursively(elements_copy[1:]):
            new_permutation = elements_copy[0] + ''.join(combination)
            permutations.append(new_permutation)

    return permutations


def _switch_cells(elements, first_index, second_index):
    elements[first_index], elements[second_index] = elements[second_index], elements[first_index]