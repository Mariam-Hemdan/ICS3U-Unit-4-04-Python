#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This module uses a break statement

import random


def main():
    # This function uses a break statement

    # input
    random_number = random.randint(1, 9+1)  # a number between 1 and 10
    number_guessing_game = int(input("Enter a number: "))
    print("")

    # process
    while True:
        if number_guessing_game == random_number:
            print("you guess it right")
            break


if __name__ == '__main__':
    main()
