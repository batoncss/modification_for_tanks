import configparser
from os import path
from modules.user_data import user_information
from modules.team_data import team_reserves
import json

config = configparser.ConfigParser()
config.read('settings.ini')
application_id = config['Application']['id']
if not path.exists('user_data.json'):
    user_information(application_id)
with open("user_data.json", "r") as read_file:
    user_data = json.load(read_file)
user_token = user_data['token']['access_token']
team_reserves_data = team_reserves(application_id, user_token)
for i in team_reserves_data:
    print(i)