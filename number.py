#!/usr/bin/env python3

# Created by: venika Sem
# Created on: Dec 2022
# This program uses a list as a parameter

import random


def find_largest_number(list_of_numbers):
    largest_number = list_of_numbers[0]

    for counter in range(0, len(list_of_numbers)):
        if list_of_numbers[counter] > largest_number:
            largest_number = list_of_numbers[counter]

    return largest_number


def main():
    # this function generates 10 random numbers

    random_numbers = []

    for loop_counter in range(0, 10):
        single_random_number = random.randint(0, 100)
        random_numbers.append(single_random_number)
        print(
            "The random number {0} is: {1}".format(
                loop_counter + 1, random_numbers[loop_counter]
            )
        )

    # calls function
    largest_number = find_largest_number(random_numbers)
    print("")
    print("The largest number is {0}".format(largest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
