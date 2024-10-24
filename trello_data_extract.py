#pip install requests

#imports
import requests
import os
import json


DIR_PATH= os.path.abspath('.')
CONFIG_FILE= os.path.join(DIR_PATH, 'trello_API_KEY.json')


# Code
def load_config():
    with open(CONFIG_FILE) as f:
        config = json.load(f)
    return config['API_KEY'], config['API_TOKEN']



# Base URL for Trello API
BASE_URL = 'https://api.trello.com/1'

def get_boards(api_key, api_token):
    url = f'{BASE_URL}/members/me/boards'
    query = {
        'key': api_key,
        'token': api_token
    }

    response = requests.get(url, params=query)

    if response.status_code == 200:
        boards = response.json()
        for board in boards:
            print(f"Board Name: {board['name']}, ID: {board['id']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':

    API_KEY, API_TOKEN= load_config()
    get_boards(API_KEY, API_TOKEN)
