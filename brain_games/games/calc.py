#!/usr/bin/env python3

# Import libraries
import brain_games.cli as cli
from random import randint, choice


# Ask for name and welcome user
cli.welcome_user()

# Define empty list for questions
questions = []

# Tuple of operators
operators_tuple = ('+', '-', '*')

# generate random numbers and operations for question
random_values = tuple((randint(1, 9), randint(1, 9),
                       choice(operators_tuple)) for _ in range(3))

# Generate questions and answers strings add to questions lists
for item in random_values:
    question = f'{item[0]} {item[2]} {item[1]}'
    answer = str(eval(question))
    questions.append((question, answer))

# game rules
game_rules = 'What is the result of the expression?'
