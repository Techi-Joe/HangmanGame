import random

def process_words(response):
    # Read words from response
    # {'word': 'forest', 'score': 39561054, 'tags': ['syn', 'n', 'results_type:primary_rel']}
    word_list = []
    for word in response:
        word_list.append(word['word'])
    return word_list

def choose_random_word(word_list):
    # Choose a random word
    return random.choice(word_list)