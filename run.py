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
WORDS = ["BEER", "PIZZA", "MOON", "WORLD", "MONKEY", "SNAKE", "APPLE", "RIVER", "SAND", "SHIP", "MOTORBIKE", "AIRPLANE"]

MAX_WRONG = len(HANGMAN) - 1

# Initialize variables

# Pick a word
word = random.choice(WORDS)

# Dashes for each letter in a word
current_guess = "-" * len(word)

# Wrong guess counter
wrong_guess = 0

# Used letters tracker
used_letters = []

# Main loop
print("Welcome to Hangman")
print("Try to guess the word!")

while wrong_guess < MAX_WRONG and current_guess != word:
    print(HANGMAN[wrong_guess])
    print(f"You have used the following letters: {used_letters}")
    print("So far the word is: ", current_guess)

    guess = input("Enter your letter guess: ").upper()

    # Check if letter already used
    while guess in used_letters:
        print(f"You have already used |{guess}| letter")
        guess = input("Enter your letter guess: ").upper()

    # Add guessed letter to used letters list
    used_letters.append(guess)

    # Check guess
    if guess in word:
        print("You have guessed correctly!")

        # Give a new version of the word mixed with letters and dashes
        new_current_guess = ""

        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]

        current_guess = new_current_guess

    else:
        print("Sorry that is incorrect letter")

        # Increase the numuber of incorrect by 1
        wrong_guess += 1

# End the game
if wrong_guess == MAX_WRONG:
    print(HANGMAN[wrong_guess])
    print("You have been hanged!")
    print("The correct word was", word)

else:
    print("You have won!")