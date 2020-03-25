import algorithms.creation_algorithms as creation_algorithms
import algorithms.pattern_algorithms as pattern_algorithms
from random import choice, randint, shuffle
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


def main():
    random_string = random_string_of_size(1000000)
    random_numbers = random_int_list_of_size(1000000)
    random_binary_string = random_binary_string_of_size(1000000)
    small_random_string = random_string_of_size(8)
    while not is_unique(small_random_string):
        small_random_string = random_string_of_size(8)

    start_time = time()
    trimmed_string = creation_algorithms.create_trimmed_string(random_string)
    finish_time = time()
    print("trimmed_string: ", trimmed_string)
    print("time ellapsed: ", finish_time - start_time)

    start_time = time()
    biggest_numbers = pattern_algorithms.find_n_biggest_numbers(random_numbers)
    finish_time = time()
    print("biggest numbers: ",biggest_numbers)
    print("time ellapsed: ", finish_time - start_time)

    start_time = time()
    palindrome = pattern_algorithms.find_longest_palindrome(random_binary_string)
    finish_time = time()
    print("palindrome: ", palindrome)
    print("time ellapsed: ", finish_time - start_time)
    
    start_time = time()
    permutations = creation_algorithms.generate_permutations_recursively(small_random_string)
    finish_time = time()
    print("recursive permutations: ", permutations)
    print("time ellapsed: ", finish_time - start_time)

    start_time = time()
    permutations = creation_algorithms.generate_permutations_iterably(small_random_string)
    finish_time = time()
    print("iterative permutations: ", permutations)
    print("time ellapsed: ", finish_time - start_time)


if __name__ == "__main__":
    main()