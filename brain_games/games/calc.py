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
    math_operator = choice(OPERATORS_TUPLE)

    # Generate questions and answers strings add to questions lists
    question = f'{random_num1} {math_operator} {random_num2}'
    answer = calculate(random_num1, random_num2, math_operator)

    return question, answer


def calculate(random_num1, random_num2, math_operator):
    if math_operator == '+':
        answer_result = str(random_num1 + random_num2)
    elif math_operator == '-':
        answer_result = str(random_num1 - random_num2)
    else:
        answer_result = str(random_num1 * random_num2)

    return answer_result
