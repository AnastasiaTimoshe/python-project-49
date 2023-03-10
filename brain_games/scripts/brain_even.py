#!/usr/bin/env python3

# Import libraries
import brain_games.cli as cli
from random import randint
from brain_games.scripts.brain_engine import run_game


def main():
    # Ask for name and welcome user
    cli.welcome_user()

    # Define empty list for questions
    questions = []

    # Tuple of random numbers
    nums = tuple(randint(1, 99) for _ in range(3))

    # generate list of questions and answers
    for item in nums:
        if item % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        questions.append((item, answer))

    # print game rules
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Run game with questions
    run_game(questions)


if __name__ == '__main__':
    main()
