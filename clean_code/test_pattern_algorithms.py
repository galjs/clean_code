from pattern_algorithms import find_longest_palindrome
from pattern_algorithms import find_n_biggest_numbers
from pattern_algorithms import generate_permutations_iterably
from pattern_algorithms import generate_permutations_recursively
from pattern_algorithms import create_trimmed_string
from random import choice, randint, shuffle
from string import digits

def random_string_of_size(n):
    return ''.join(choice(digits) for i in range(n))


def random_binary_string_of_size(n):
    return ''.join(choice(['0', '1']) for i in range(n))


def random_int_list_of_size(n):
    return list(map(lambda _: randint(0, n), range(n)))


def run_algorithms():
    random_string = random_string_of_size(1000000)
    random_numbers = random_int_list_of_size(1000000)
    random_binary_string = random_binary_string_of_size(1000000)
    small_random_string = random_string_of_size(7)

    trimmed_string = create_trimmed_string(random_string)
    print("trimmed_string: ", trimmed_string)

    biggest_numbers = find_n_biggest_numbers(random_numbers)
    print("biggest numbers: ",biggest_numbers)

    palindrome = find_longest_palindrome(random_binary_string)
    print("palindrome: ", palindrome)

    permutations = generate_permutations_recursively(small_random_string)
    print("recursive permutations: ", permutations)

    permutations = generate_permutations_iterably("abcde")
    print("iterative permutations: ", permutations)


def main():
    run_algorithms()


if __name__ == "__main__":
    main()
