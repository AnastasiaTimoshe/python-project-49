#!/usr/bin/env python3

# Import libraries
import brain_games.cli as cli
from random import randint
from brain_games.scripts.brain_engine import run_game
from math import gcd


def main():
    # Ask for name and welcome user
    cli.welcome_user()

    # Define empty list for questions
    questions = []

    # Tuple of random numbers
    nums = tuple((randint(1, 20), randint(1, 20)) for _ in range(3))

    # generate list of questions and answers
    for item in nums:
        answer = str(gcd(item[0], item[1]))
        question = f'{item[0]} and {item[1]}'
        questions.append((question, answer))

    # print game rules
    print('Find the greatest common divisor of given numbers.')

    # Run game with questions
    run_game(questions)


if __name__ == '__main__':
    main()
