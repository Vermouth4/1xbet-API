import requests
import json
from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text
"""
This code was developed for the purpose of hacking the casino and creating many requests on it and stopping it. This is a group of requests and breaking the protection.

|	This script was formatted by Vermouth.


You need a session key to use it and extract it from https://github.com/BettingApi/docs#readme





"""
class XBetAPI:
    def __init__(self):
        self.config = self.load_config()
        self.base_url = self.config['api_url']
        self.secret_key = self.config['secret_key']
        if not self.secret_key:
            raise ValueError("Secret key is required.")
        self.headers = {
            'Authorization': f'Bearer {self.secret_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'XBetAPI/1.0'
        }
        self.console = Console()
        self.display_welcome_message()

    def load_config(self):
        with open('config.json') as config_file:
            return json.load(config_file)

    def request(self, endpoint, params=None):
        try:
            response = requests.get(f'{self.base_url}/{endpoint}', headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def display_welcome_message(self):
        figlet = Figlet(font='starwars')
        text = figlet.renderText('By Vermouth')
        self.console.print(Text(text, style='bold yellow on black'))

    def get_live_all(self):
        return self.request('football/live')

    def get_live_single_match(self, match_id):
        return self.request(f'football/live/{match_id}')

    def get_live_leagues(self):
        return self.request('football/live/leagues')

    def get_live_league_matches(self, league_id):
        return self.request(f'football/live/leagues/{league_id}/matches')

    def get_prematch_all(self):
        return self.request('football/prematch')

    def get_prematch_single(self, match_id):
        return self.request(f'football/prematch/{match_id}')

    def get_prematch_leagues(self):
        return self.request('football/prematch/leagues')

    def get_prematch_league_matches(self, league_id):
        return self.request(f'football/prematch/leagues/{league_id}/matches')

    def get_match(self, match_id):
        return self.request(f'football/matches/{match_id}')

    def get_info(self):
        return self.request('info')

if __name__ == '__main__':
    xbet_api = XBetAPI()
    live_matches = xbet_api.get_live_all()
    print(live_matches)
    match_id = 255860098
    live_match_details = xbet_api.get_live_single_match(match_id)
    print(live_match_details)
