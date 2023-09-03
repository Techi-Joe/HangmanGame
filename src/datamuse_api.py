import requests

url = "https://api.datamuse.com/words?topics="

def fetch_words_from_api(topic):
    # API request
    return requests.get(url + topic.lower(), timeout=5)
