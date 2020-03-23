from missing_number import find_missing_number
from random import shuffle, choice

"""Gets a number from the user, creates a list of length Number with the numbers
   0-Number and then randomly removes a number. then finds which number
   was removed."""

def get_number_from_user():
    number = input("enter a whole number to be used as generator of a list 0-number: ")
    try:
        number = int(number)
    except ValueError:
        raise ValueError("input must be an integer")
    if number < 0:
        raise ValueError("number must be greater or equal to 0")

    return number


def create_list_with_missing_number(max_value):
    numbers = list(range(max_value+1))
    shuffle(numbers)
    numbers.remove(choice(numbers))
    return numbers


def main():
    chosen_number = get_number_from_user()
    numbers = create_list_with_missing_number(chosen_number)
    deleted_number = find_missing_number(numbers)
    print(deleted_number)

if __name__ == "__main__":
    main()