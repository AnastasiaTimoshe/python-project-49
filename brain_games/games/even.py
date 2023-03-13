#!/usr/bin/env python3

# Import libraries
from random import randint


# game rules
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

# Number limits
MIN_NUM = 1
MAX_NUM = 99


def generate_question():
    # Tuple of random numbers
    num = randint(MIN_NUM, MAX_NUM)
    question = str(num)

    # generate list of questions and answers
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
