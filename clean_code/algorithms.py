from random import choice, randint, shuffle
from string import digits
from time import time


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


def run_algorithms():
    random_string = random_string_of_size(1000000)
    starting_time = time()
    print_trimmed_string(random_string)
    time_ellapsed = time() - starting_time
    print("trimmed_string: ", time_ellapsed)

    random_numbers = random_int_list_of_size(1000000)
    starting_time = time()
    print_n_biggest_numbers(random_numbers)
    time_ellapsed = time() - starting_time
    print("biggest numbers: ",time_ellapsed)
    


def main():
    run_algorithms()


if __name__ == "__main__":
    main()