#!/usr/bin/env python3

# Import libraries
import brain_games.cli as cli
from random import randint, choice
from brain_games.scripts.brain_engine import run_game


def main():
    # Ask for name and welcome user
    cli.welcome_user()

    # Define empty list for questions
    questions = []

    # Tuple of operators
    operators_tuple = ('+', '-', '*')

    # generate random numbers and operations for question
    random_values = tuple((randint(1, 9), randint(1, 9), choice(operators_tuple)) for _ in range(3))

    # Generate questions and answers strings add to questions lists
    for item in random_values:
        question = f'{item[0]} {item[2]} {item[1]}'
        answer = str(eval(question))
        questions.append((question, answer))

    # print game rules
    print('What is the result of the expression?')

    # Run game with questions
    run_game(questions)


if __name__ == '__main__':
    main()
