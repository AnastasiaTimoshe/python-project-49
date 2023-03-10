import prompt
username = ''


def welcome_user():
    print('Welcome to the Brain Games!')
    global username
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
