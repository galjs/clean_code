from math import factorial

"""This module supplies fast algorithms for pattern-related creations:
   all permutations of a staring, duplicate-deletion."""

def create_trimmed_string(base_string):
    """deletes duplicates in a string. example: aaabbaac -> abac"""
    trimmed_elements = []
    trimmed_elements.append(base_string[:1])
    for index in range(1, len(base_string)):
        if base_string[index] != base_string[index-1]:
            trimmed_elements.append(base_string[index])
    return ''.join(trimmed_elements)


def generate_permutations_iterably(elements):
    """returns all the permutations of a string. the function is non-recursive"""
    permutations = set()
    final_set = set()
    expectd_permutations_number = factorial(len(elements))

    new_combinations = _first_cell_permutations(elements)
    permutations.update(new_combinations)

    while len(final_set) < expectd_permutations_number:
        permutations_copy = permutations.copy()
        permutations = set()

        for permutation in permutations_copy:
            new_combinations = _first_cell_permutations(permutation)
            # the first permutation is the same as "permutation", so there
            # is no need to add it again

            permutations.update(new_combinations[1:])

        final_set.update(permutations)

    return final_set


def _first_cell_permutations(base_state):
    new_permutations = []
    for index in range(len(base_state)):
        splitted_base_state = list(base_state)
        _switch_cells(splitted_base_state, 0, index)
        new_permutations.append(''.join(splitted_base_state))

    return new_permutations


def _switch_cells(elements, first, second):
    elements[first], elements[second] = elements[second], elements[first]


def generate_permutations_recursively(base_string):
    """returns all the permutations of a string. the function is recursive"""
    return _generate_permutations_recursively(list(base_string))


def _generate_permutations_recursively(elements):
    permutations = []
    if len(elements) == 1:
        return elements

    for permutation in _first_cell_permutations(elements):
        for combination in _generate_permutations_recursively(permutation[1:]):
            new_permutation = permutation[0] + combination
            permutations.append(new_permutation)

    return permutations