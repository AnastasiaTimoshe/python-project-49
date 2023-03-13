#!/usr/bin/env python3

# Import libraries
from random import randint

# game rules
GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# Number limits
MIN_NUM = 2
MAX_NUM = 100


# check numbers for even
def is_prime(num_to_check):
    # divide the number by the range to the number itself
    for i in range(2, num_to_check):
        if (num_to_check % i) == 0:
            return 'no'
    return 'yes'


def generate_question():
    # generate random number for question
    random_values = randint(MIN_NUM, MAX_NUM)

    # Generate question and answer strings
    answer = is_prime(random_values)
    question = str(random_values)

    return question, answer
