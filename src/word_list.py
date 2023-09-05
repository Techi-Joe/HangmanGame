import random

def process_words(response):
    # Read words from response
    word_list = []
    rejected_words = []
    for word in response:
        # prioritizes words with high frequency and high score
        if get_word_frequency(word) > 1.00 and get_word_score(word) > 25000000:
            word_list.append(word['word'])

            #!
            # print(f"added word {word['word']} with frequency {get_word_frequency(word)} and score {get_word_score(word)}")

        else:
            rejected_words.append(word['word'])
    # if no words with a frequency >1 and no score greater than 29550000 is found, then we accept all words
    if len(word_list) == 0:
        print("\nUnfortunately that topic is either not broad or not common enough, so the word may not quite match the topic you picked.")
        return rejected_words
    return word_list


def get_word_frequency(word):
    # Get the frequency of a word
    tags = word.get("tags", [])
    for tag in tags:
        if tag.startswith("f:"):
            try:
                frequency_string = tag[2:]
                if frequency_string:
                    return float(frequency_string)
            except ValueError:
                pass  # Handle cases where the frequency value is not a valid float
    # If no valid frequency tag is found, return a default frequency value
    return 1.01


def get_word_score(word):
    # Check if the 'score' key exists in the word object
    if 'score' in word:
        try:
            # Convert the score value to an integer
            score = int(word['score'])
            return score
        except ValueError:
            # Handle cases where the score is not a valid integer
            return None
    else:
        # Handle cases where the 'score' key is missing in the JSON object
        return 30000000

def choose_random_word(word_list):
    # Choose a random word
    return random.choice(word_list)