import datamuse_api
import word_list
'''
topics = ["sports", "animals", "farm", "nature", "travel", "weather", "family",
          "science", "food", "history", "movies", "music", "literature", "art", "technology", "audio"]
'''

topics = ["art"]

def test_topics():
    for topic in topics:
        print(f"\nTopic: {topic}")
        api_response = datamuse_api.fetch_words_from_api(topic)
        word_list.process_words(api_response, topic, debug=True)

def main():
    test_topics()


if __name__ == "__main__":
    main()