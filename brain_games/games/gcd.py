#!/usr/bin/env python3

# Import libraries
import brain_games.cli as cli
from random import randint
from math import gcd


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

# game rules
game_rules = 'Find the greatest common divisor of given numbers.'
