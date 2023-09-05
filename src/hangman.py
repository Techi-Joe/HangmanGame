"""
Hangman Game Class

This class represents a simple Hangman game. 
It allows the player to pick a topic for the computer to choose a word from
and then the player attempts to guess the word within a limited number of attempts.

Attributes:
    word (str): The word the player needs to guess.
    guessed_letters (set): A set of letters the player has guessed.
    max_attempts (int): The maximum number of incorrect guesses allowed.
    remaining_attempts (int): The number of remaining attempts.


Methods:
    __init__(self): Initializes a new HangmanGame instance.
    play(self): Starts and manages the game loop.
    display_text(self, text): Displays text to the player and waits for a key press to continue.
    display_word(self): Displays the word with guessed letters revealed.
    display_guessed_letters(self): Displays the letters guessed so far.
    make_guess(self, letter): Handles a player's guess.
    check_win(self): Checks if the player has won.
    check_loss(self): Checks if the player has lost.
"""


from colorama import Fore, Style, init
import datamuse_api
import word_list

# Initialize colorama (required for Windows)
init(autoreset=True)

class HangmanGame:
    def __init__(self):
        self.word = ""
        self.guessed_letters = set()
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts

    def play(self):

        # Main game loop and logic


        # intro text explaining the game
        intro_texts = ["Welcome to Hangman Game, designed by Techi-Joe!", "This version of the classic napkin game allows you to pick a topic for the computer to choose a word from.", "Then it's up to you to quess the computer's word before you run out of lives!"]
        for text in intro_texts:
            self.display_text(text)


        # ask user for a topic and validate their response
        inputError = True
        while inputError:
            print("\nPlease enter a topic (nouns are best): ", end="")
            input_topic = input()
            if not input_topic.isalpha():
                inputError = True
                self.display_text("Error: " + input_topic + " is not a valid topic")
            else:
                inputError = False


        # send topic to datamuse_api.pyinput_topic and get a random word
        api_response = datamuse_api.fetch_words_from_api(input_topic)
        word = word_list.choose_random_word(word_list.process_words(api_response))

        #!
        print("word: " + word)


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