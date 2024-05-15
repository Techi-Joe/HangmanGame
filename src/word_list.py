import random
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

def calculate_similarity(word, topic):
    # Calculate cosine similarity between word and topic
    word_vector = nlp(word).vector
    topic_vector = nlp(topic).vector
    similarity = word_vector.dot(topic_vector) / (nlp(word).vector_norm * nlp(topic).vector_norm)
    return similarity

def process_words(response, topic, debug=False):
    # Read words from response
    word_list = []
    rejected_words = []

    # Calculate average frequency and score
    average_frequency = sum(get_word_frequency(word) for word in response) / len(response)
    average_score = sum(get_word_score(word) for word in response) / len(response)

    # Adjust thresholds based on averages
    frequency_threshold = 0.7*average_frequency
    score_threshold = 0.9*average_score

    # Additional similarity threshold
    similarity_threshold = 0.4  # Adjust as needed

    # Filter words based on adjusted thresholds and similarity
    for word in response:
        word_frequency = get_word_frequency(word)
        word_score = get_word_score(word)

        if (
            word_frequency > frequency_threshold
            and word_score > score_threshold
            and calculate_similarity(word['word'], topic) > similarity_threshold
        ):
            word_list.append(word['word'])

            if debug:
                print(f"added word {word['word']} with frequency {word_frequency}, score {word_score}, and similarity {calculate_similarity(word['word'], topic)} under topic {topic}")

        else:
            rejected_words.append(word['word'])

    # If no words meet the adjusted thresholds, accept all words
    if len(word_list) < 5:
        print("\nUnfortunately, that topic is either not broad or not common enough, so the words may not quite match the topic you picked.")

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
    try:
        return random.choice(word_list)
    except IndexError:
        input("\nERROR: INVALID TOPIC. PRESS ENTER TO EXIT")
        