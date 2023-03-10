#!/usr/bin/env python3

# Import libraries
from brain_games.scripts.brain_engine import run_game
from brain_games.games import progression


def main():
    # Run game with questions
    run_game(progression)


if __name__ == '__main__':
    main()
