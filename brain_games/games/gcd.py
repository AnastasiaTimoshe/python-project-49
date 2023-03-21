#!/usr/bin/env python3

# Import libraries
from random import randint
from math import gcd


# game rules
GAME_RULES = 'Find the greatest common divisor of given numbers.'

# Number limits
MIN_NUM = 1
MAX_NUM = 20


# generate list of questions and answers
def generate_question():
    random_num1 = randint(MIN_NUM, MAX_NUM)
    random_num2 = randint(MIN_NUM, MAX_NUM)
    question = f'{random_num1} {random_num2}'
    answer = str(gcd(random_num1, random_num2))

    return question, answer
