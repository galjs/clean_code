from random import choice, randint, shuffle
from string import digits
from time import time
from collections import Counter
from math import factorial


def random_string_of_size(n):
    return ''.join(choice(digits) for i in range(n))


def random_binary_string_of_size(n):
    return ''.join(choice(['0', '1']) for i in range(n))


def random_int_list_of_size(n):
    return list(map(lambda _: randint(0, n), range(n)))


def permutations(base_string):
    pass


def print_n_biggest_numbers(numbers, amount=20):
    if len(numbers) > amount:
        biggest_numbers = sorted(numbers[:amount], reverse=True)
    else:
        return numbers


    for number in numbers:
        if number > biggest_numbers[-1]:
            add_number_to_sorted_list(biggest_numbers, number)
            del biggest_numbers[-1]

    print(biggest_numbers)


def add_number_to_sorted_list(numbers, number):
    for index in range(len(numbers)):
        if number > numbers[index]:
            numbers.insert(index, number)
            return
    numbers.append(number)


def print_trimmed_string(base_string):
    return ''.join(base_string[i] for i in range(1, len(base_string)) if base_string[i] != base_string[i-1])


def print_longest_palindrome(base_string):
    longest_length = 0
    longest_start = 0
    odd = True

    for index in range(len(base_string) - 1):
        current_length = odd_palindrome_length(base_string, index)
        if current_length > longest_length:
            longest_length = current_length
            longest_start = index
            odd = True

        if current_length == 1 and base_string[index] == base_string[index+1]:
            current_length = even_palindrome_length(base_string, index, index+1)
            if current_length > longest_length:
                longest_length = current_length
                longest_start = index
                odd = False

    if odd:
        print(base_string[longest_start-int(longest_length/2):longest_start+int(longest_length / 2)+1])
    else:
        print(base_string[longest_start-int(longest_length/2)+1:longest_start+int(longest_length / 2)+1])


def odd_palindrome_length(base_string, middle):
    length = 1
    distance = 1
    while distance + middle < len(base_string) and middle >= distance:
        if base_string[middle + distance] == base_string[middle - distance]:
            length += 2
            distance += 1
        else:
            break
    return length


def even_palindrome_length(base_string, middle_left, middle_right):
    length = 2
    distance = 1
    while distance + middle_right < len(base_string) and middle_left >= distance:
        if base_string[middle_right + distance] == base_string[middle_left - distance]:
            length += 2
            distance += 1
        else:
            break
    return length


def print_permutations(base_string):
    elements = list(base_string)
    limit = factorial(len(elements))
    indexes = [0]*len(elements)
    permutations = []
    possible_permutations_with_repetition = len(elements) ** len(elements)
    possible_permutations_with_repetition -= (possible_permutations_with_repetition / len(elements))

    for permutation in range(limit):
        permutations.append([])
        while not is_unique(indexes):
            increase_indexes(indexes, len(elements) - 1)

        for index in indexes:
            permutations[permutation].append(elements[index])
        increase_indexes(indexes, len(elements)-1)

    for permutation in permutations:
        print(''.join(permutation))



def is_unique(indexes):
    occurences = Counter(indexes)
    for times in occurences.values():
        if times > 1:
            return False
    return True


def increase_indexes(indexes, max_index_value):
    current_index = 0
    indexes[current_index] += 1
    if indexes[current_index] <= max_index_value:
        return

    while current_index < len(indexes) - 1 and indexes[current_index] > max_index_value:
        indexes[current_index] = 0
        current_index += 1
        indexes[current_index] += 1

    if indexes[-1] > max_index_value:
        raise IndexError("index out of range")


def run_algorithms():
    #random_string = random_string_of_size(1000000)
    #starting_time = time()
    #print_trimmed_string(random_string)
    #time_ellapsed = time() - starting_time
    #print("trimmed_string: ", time_ellapsed)

    #random_numbers = random_int_list_of_size(1000000)
    #starting_time = time()
    #print_n_biggest_numbers(random_numbers)
    #time_ellapsed = time() - starting_time
    #print("biggest numbers: ",time_ellapsed)

    #random_binary_string = random_binary_string_of_size(1000000)
    #starting_time = time()
    #print_longest_palindrome(random_binary_string)
    #time_ellapsed = time() - starting_time
    #print("palindromes: ",time_ellapsed)

    random_string = random_string_of_size(6)
    starting_time = time()
    print_permutations(random_string)
    time_ellapsed = time() - starting_time
    print("permutations: ",time_ellapsed)
    


def main():
    run_algorithms()


if __name__ == "__main__":
    main()