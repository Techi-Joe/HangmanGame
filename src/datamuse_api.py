import requests

url = "https://api.datamuse.com/words?"

def fetch_words_from_api(topic):
    # API request
    try:
        response = requests.get(url + "ml=" + topic.lower() + "&md=f", timeout=5)

        # Check the status code and process the response as needed
        if response.status_code == 200:
            return response.json()
        else:
            print("\nRequest failed with status code: ", response.status_code)
            return None

    except requests.exceptions.Timeout:
        print("\nRequest timed out. Please check your internet connection or try again later.")
        return None
    
    except requests.exceptions.ConnectionError:
        print("\n! Connection error. Please check your internet connection or try again later. !")
        return None
