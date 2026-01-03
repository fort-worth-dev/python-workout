"""
Exercise 1: Guessing Game

From "Python Workout" by Reuven M. Lerner - Chapter 2: Strings

Problem:
Write a function that generates a random number between 0 and 100, then
repeatedly asks the user to guess the number. After each guess, provide
feedback indicating whether the guess was too high, too low, or correct.

Learning Objectives:
- Working with user input using input()
- Converting strings to integers
- Using the random module
- Implementing game loop logic
- Providing user feedback with print()

Difficulty: Beginner
"""

import random


def guessing_game() -> None:
    """
    Interactive number guessing game.

    Generates a random number between 0 and 100 (inclusive) and prompts
    the user to guess it. Provides feedback after each guess:
    - "Too high" if guess is greater than the target
    - "Too low" if guess is less than the target
    - "Just right!" when the user guesses correctly

    The game continues until the user guesses the correct number.

    Returns:
        None: This function is interactive and has no return value.

    Examples:
        >>> guessing_game()  # doctest: +SKIP
        Guess a number (0-100): 50
        Too high
        Guess a number (0-100): 25
        Too low
        Guess a number (0-100): 37
        Just right!
    """
    target = random.randint(0, 100)

    while True:
        user_input = input("Guess a number (0-100): ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number")
            continue

        if guess > target:
            print("Too high")
        elif guess < target:
            print("Too low")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    guessing_game()