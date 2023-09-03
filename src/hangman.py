'''
This is the hangman module for running the
primary game loop.
'''

import time
from colorama import Fore, Back, Style, init
import datamuse_api

class HangmanGame:
    def __init__(self):
        self.word = ""
        self.guessed_letters = set()
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts

    def play(self):

        # Main game loop and logic

        # intro text explaining the game
        intro_texts = ["Welcome to Hangman Game, designed by Techi-Joe!", "This version of the classic napkin game\nallows you to pick topics for the computer\nto choose a word from.", "Unfortunately the words the computer comes up with are a bit\nunrelated sometimes, but hey, thats why you have multiple lives!"]
        for text in intro_texts:
            self.display_text(text)

    def display_text(self, text):
        # Display the text using a enter to continue method
        print(Fore.GREEN + "\r\n" + text)
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