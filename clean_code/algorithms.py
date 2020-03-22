from random import choice, randint, shuffle
from string import digits
from time import time


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

    def print_trimmed_string(self, base_string):
        trimmed_string = base_string[0]
        for index in range(1, len(base_string)):
            #if base_string[index] != trimmed_string[-1]:
            #    trimmed_string += base_string[index]
            pass

        #print(trimmed_string)

    def run_algorithms(self):
        random_string = self.random_string_of_size(10000000)
        starting_time = time()
        self.print_trimmed_string(random_string)
        time_ellapsed = time() - starting_time
        print(time_ellapsed)

def main():
    tester = Algorithms()
    tester.run_algorithms()


if __name__ == "__main__":
    main()