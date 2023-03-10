#!/usr/bin/env python3
import brain_games.cli as cli


def run_game(game_module):
    print(game_module.game_rules)
    for question in game_module.questions:
        print('Question: ' + str(question[0]))
        answer_user = input('Your answer: ')
        if question[1] == answer_user:
            print('Correct!')
        else:
            print(f"{answer_user} is wrong answer ;(. "
                  f"Correct answer was {question[1]}. "
                  f"Let's try again, {cli.username}!")
            quit()
    print(f'Congratulations, {cli.username}!')
