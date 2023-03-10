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

    # generate random numbers and operations for question
    random_values = tuple(randint(2, 100) for _ in range(3))

    # Generate questions and answers strings add to questions lists
    for item in random_values:
        answer = is_prime(item)
        questions.append((item, answer))

    # print game rules
    print('What is the result of the expression?')

    # Run game with questions
    run_game(questions)


def is_prime(num_to_check):
    for i in range(2, num_to_check):
        if (num_to_check % i) == 0:
            return 'no'
        return 'yes'


if __name__ == '__main__':
    main()
