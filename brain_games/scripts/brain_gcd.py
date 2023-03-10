#!/usr/bin/env python3

# Import libraries
from brain_games.scripts.brain_engine import run_game
from brain_games.games import gcd


def main():
    # Run game with questions
    run_game(gcd)


if __name__ == '__main__':
    main()
