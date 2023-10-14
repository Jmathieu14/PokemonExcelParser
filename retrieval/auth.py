from pokemontcgsdk import RestClient
from pathlib import Path

API_KEY_FILE_NAME = 'pokemon-tcg-api-key.txt'


def init_api_auth():
    with open(Path.home() / 'OneDrive' / 'Documents' / 'api' / API_KEY_FILE_NAME) as file:
        key = file.readline()
        RestClient.configure(key)
        print('RestClient configured with user\'s api key')
