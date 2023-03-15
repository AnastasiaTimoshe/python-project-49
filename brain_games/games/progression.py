#!/usr/bin/env python3

# Import libraries
from random import randint


# game rules
GAME_RULES = 'What number is missing in the progression?'

# Number limits
START_MIN_NUM = 0
START_MAX_NUM = 20
STEP_MIN_NUM = 2
STEP_MAX_NUM = 10
PROGRESSION_MIN_NUM = 6
PROGRESSION_MAX_NUM = 10


def generate_question():
    step = randint(STEP_MIN_NUM, STEP_MAX_NUM)
    progression_len = randint(PROGRESSION_MIN_NUM, PROGRESSION_MAX_NUM)
    start = randint(START_MIN_NUM, START_MAX_NUM)
    stop = start + step * progression_len

    # List of random numbers
    nums = list(i for i in range(start, stop, step))

    # define index of number in progression which we want to hide
    random_index = randint(0, len(nums) - 1)
    answer = str(nums[random_index])
    nums[random_index] = '..'

    # define variable to store question
    question = ''

    # generate list of questions and answers
    for item in nums:
        question = question + str(item) + ' '

    return question, answer
