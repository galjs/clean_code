
import random


class InputError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return self.message


def get_number_from_user():
    number = input("enter a whole number: ")
    try:
        number = int(number)
    except:
        raise InputError("input must be an integer")
    if number < 0:
        raise InputError("number must be greater or equal to 0")

    return number


def create_list_with_missing_number(max_value):
    numbers = list(range(max_value+1))
    random.shuffle(numbers)
    numbers.remove(random.choice(numbers))
    return numbers


def sum_arithmetic_progress(difference, first_element, number_of_elements):
    total = (number_of_elements * (2 * first_element + difference * (number_of_elements - 1))) / 2
    return total


def main():
    chosen_number = get_number_from_user()
    total = sum_arithmetic_progress(1, 1, chosen_number)
    numbers = create_list_with_missing_number(chosen_number)
    missing_number = total - sum(numbers)
    print(missing_number)

if __name__ == "__main__":
    main()