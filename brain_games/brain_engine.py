import prompt


NUM_OF_TRIES = 3


def run_game(game_module):
    # Ask for name and welcome user
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')

    print(game_module.GAME_RULES)

    for _ in range(NUM_OF_TRIES):
        question, answer = game_module.generate_question()
        print('Question: ' + question)
        answer_user = input('Your answer: ')
        if answer == answer_user:
            print('Correct!')
        else:
            print(f"{answer_user} is wrong answer ;(. "
                  f"Correct answer was {answer}. "
                  f"Let's try again, {username}!")
            quit()
    print(f'Congratulations, {username}!')
