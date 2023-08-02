import requests
import os
import json
from mainUrls import urls


def characters_get(endpoint=urls, url=urls['domain']):
    response = requests.get(url + endpoint).json()
    response_ = json.dumps(response)
    return response_


def make_new_file(response_character, response_location, response_episode):
    with open(os.path.join('pythonProject1', 'lastCreatedFile.txt'), 'w') as fw:
        fw.write(
            f'{response_character}\n'
            f'{response_location}\n'
            f'{response_episode}'
        )


character_response = characters_get(urls['character'])
location_response = characters_get(urls['location'])
episode_response = characters_get(urls['episode'])

make_new_file(character_response, location_response, episode_response)
