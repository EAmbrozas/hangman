# Hangman Game
# Computer generates a random word from a list
# Player makes a letter guess at a time

# Imports
import random

# Constants
HANGMAN = ["""
    +---+
    |   |
        |
        |
        |
        |
=========""", """
    +---+
    |   |
    O   |
        |
        |
        |
=========""", """
    +---+
    |   |
    O   |
    |   |
        |
        |
=========""", """
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========""", """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========""", """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========""", """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
========="""]

# List of words that will be generated randomly by a computer
WORDS = ["BEER", "PIZZA", "MOON", "WORLD", "MONKEY", "SNAKE", "APPLE"]