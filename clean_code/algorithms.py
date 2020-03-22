from random import choice, randint, shuffle
from string import digits


class Algorithms():
    def __init__(self):
        pass

    def random_string_of_size(self, n):
        return ''.join(choice(digits) for i in range(n))

    def random_binary_string_of_size(self, n):
        return ''.join(choice(['0', '1']) for i in range(n))

    def random_int_list_of_size(self, n):
        return map(lambda _: randint(), range(n))

    def permutations(self, base_string):
        pass

    def delete_multiples_in_string(self, base_string):
        for index in range(len(base_string)):
            while index < len(base_string) - 1 and base_string[index] == base_string[index+1]:
                base_string = base_string[:index+1] + base_string[index + 2:]

        print(base_string)


    def run_algorithms(self):
        self.delete_multiples_in_string("aaabaaccd")
