import algorithms.creation_algorithms as creation_algorithms
import algorithms.pattern_algorithms as pattern_algorithms
from random import choice, randint
from string import digits
from time import time

def random_string_of_size(n):
    return ''.join(choice(digits) for _ in range(n))


def random_binary_string_of_size(n):
    return ''.join(choice(['0', '1']) for _ in range(n))


def random_int_list_of_size(n):
    return list(map(lambda _: randint(0, n), range(n)))


def is_unique(elements):
    return len(elements) == len(set(elements))


def run_and_check_time(function, *args, **kwargs):
    start = time()
    function_return_value = function(*args, ** kwargs)
    elapsed = time() - start
    print("{} took {} seconds".format(function.__name__, elapsed))
    return function_return_value


def main():
    random_string = random_string_of_size(1000000)
    random_numbers = random_int_list_of_size(1000000)
    random_binary_string = random_binary_string_of_size(1000000)
    small_random_string = random_string_of_size(8)
    while not is_unique(small_random_string):
        small_random_string = random_string_of_size(8)

    run_and_check_time(creation_algorithms.generate_permutations_recursively, small_random_string)
    run_and_check_time(creation_algorithms.generate_permutations_iterably, small_random_string)
    run_and_check_time(creation_algorithms.create_trimmed_string, random_string)
    run_and_check_time(pattern_algorithms.find_n_biggest_numbers, random_numbers)
    run_and_check_time(pattern_algorithms.find_longest_palindrome, random_binary_string)


if __name__ == "__main__":
    main()