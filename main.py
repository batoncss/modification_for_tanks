import configparser
from os import path
from user_data import user_information
import json

config = configparser.ConfigParser()
config.read('settings.ini')
application_id = config['Application']['id']
if not path.exists('user_data.json'):
    user_information(application_id)
with open("user_data.json", "r") as read_file:
    b = json.load(read_file)
print(b['token'])
