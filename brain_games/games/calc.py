#!/usr/bin/env python3

# Import libraries
from random import randint, choice


# game rules
GAME_RULES = 'What is the result of the expression?'

# Tuple of operators
OPERATORS_TUPLE = ('+', '-', '*')

# Number limits
MIN_NUM = 1
MAX_NUM = 9


def generate_question():
    # generate random numbers and operations for question
    random_num1 = randint(MIN_NUM, MAX_NUM)
    random_num2 = randint(MIN_NUM, MAX_NUM)
    math_operators = choice(OPERATORS_TUPLE)

    # Generate questions and answers strings add to questions lists
    question = f'{random_num1} {math_operators} {random_num2}'
    answer = str(eval(question))

    return question, answer
