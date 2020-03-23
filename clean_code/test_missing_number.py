import missing_number
from random import shuffle, choice


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
    shuffle(numbers)
    numbers.remove(choice(numbers))
    return numbers


def main():
    chosen_number = get_number_from_user()
    numbers = create_list_with_missing_number(chosen_number)
    deleted_number = missing_number.find_missing_number(numbers)
    print(deleted_number)

if __name__ == "__main__":
    main()