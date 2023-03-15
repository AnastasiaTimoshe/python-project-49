#!/usr/bin/env python3

# Import libraries
from brain_games.brain_engine import run_game
from brain_games.games import prime


def main():
    # Run game with questions
    run_game(prime)


if __name__ == '__main__':
    main()
