#!/usr/bin/env python3
import brain_games.cli as cli


NUM_OF_TRYS = 3


def run_game(game_module):
    # Ask for name and welcome user
    cli.welcome_user()

    print(game_module.GAME_RULES)

    for _ in range(NUM_OF_TRYS):
        question, answer = game_module.generate_question()
        print('Question: ' + question)
        answer_user = input('Your answer: ')
        if answer == answer_user:
            print('Correct!')
        else:
            print(f"{answer_user} is wrong answer ;(. "
                  f"Correct answer was {answer}. "
                  f"Let's try again, {cli.username}!")
            quit()
    print(f'Congratulations, {cli.username}!')
