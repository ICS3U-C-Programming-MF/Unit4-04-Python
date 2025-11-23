#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Nov 20th, 2025
# this program generates a random correct guess.
# and keeps asking the user
# to guess the number until they guess correctly.
# then breaks out of the loop.

import random


def main():
    # this function generates a random correct guess
    # and keeps asking the user to guess the number
    # until they guess correctly.

    # input
    correct_guess = random.randint(1, 10)
    user_guess = 0

    # process & output
    while user_guess != correct_guess:
        user_input = input("Guess a number between 1 and 10: ")
        try:
            user_guess = int(user_input)
            if user_guess < 1 or user_guess > 10:
                print("Please enter a number within the range.")
            else:
                if user_guess != correct_guess:
                    print("Incorrect guess. Try again.")
        except ValueError:
            print("That's not a valid number. Please try again.")

    print(f"Congratulations! Your guess {correct_guess} was the correct number!")
    print("\nThanks for playing!.")


if __name__ == "__main__":
    main()
