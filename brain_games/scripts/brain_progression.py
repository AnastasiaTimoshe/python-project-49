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

    #
    for _ in range(3):
        step = randint(2, 10)
        prgs_len = randint(6, 10)
        start = randint(0, 10)
        stop = start + step * prgs_len

        # Tuple of random numbers
        nums = list(i for i in range(start, stop, step))

        #
        random_index = randint(0, len(nums) - 1)
        answer = str(nums[random_index])
        nums[random_index] = '..'
        question = ''

        # generate list of questions and answers
        for item in nums:
            question = question + str(item) + ' '

        questions.append((question, answer))

    # print game rules
    print('Find the greatest common divisor of given numbers.')

    # Run game with questions
    run_game(questions)


if __name__ == '__main__':
    main()
