#!/usr/bin/env python3
import brain_games.cli as cli


def run_game(questions):
    for question in questions:
        print('Question: ' + str(question[0]))
        answer_user = input('Your answer: ')
        if question[1] == answer_user:
            print('Correct!')
        else:
            print(f"{answer_user} is wrong answer ;(. Correct answer was {question[1]}. Let's try again, {cli.username}!")
            quit()
    print(f'Congratulations, {cli.username}!')
