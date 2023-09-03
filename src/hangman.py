'''
This is the hangman module for running the
primary game loop.
'''

import time
from colorama import Fore, Back, Style, init
import datamuse_api

class HangmanGame:
    def __init__(self):
        self.word = "-1"
        self.guessed_letters = set()
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts

    def play(self):
        # Main game loop and logic
        intro_texts = ["Welcome to Hangman Game, designed by Techi-Joe!", "ahhhhhhhhhhh"]
        for i in range(len(intro_texts)):
            self.display_text(intro_texts[i])

    def display_text(self, text):
        # Display the text using a enter to continue method
        print(Fore.GREEN + "\r" + text)
        print(Fore.LIGHTBLACK_EX + "Press enter to continue...", end="", flush=True)
        input()
        print(Style.RESET_ALL + "\033[A", end="")
        print("\r                          ", end="")

    def display_word(self):
        # Display the word with guessed letters revealed
        return 0
    def display_guessed_letters(self):
        # Display the letters guessed so far
        return 0
    def make_guess(self, letter):
        # Handle a player's guess
        return 0
    def check_win(self):
        # Check if the player has won
        return 0
    def check_loss(self):
        # Check if the player has lost
        return 0