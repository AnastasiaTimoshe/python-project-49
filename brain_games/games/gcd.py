#!/usr/bin/env python3

# Import libraries
from random import randint
from math import gcd


# game rules
GAME_RULES = 'Find the greatest common divisor of given numbers.'

# Number limits
MIN_NUM = 1
MAX_NUM = 20


def generate_question():
    # Tuple of random numbers
    nums = tuple((randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)))

    # generate list of questions and answers
    answer = str(gcd(nums[0], nums[1]))
    question = f'{nums[0]} {nums[1]}'

    return question, answer
