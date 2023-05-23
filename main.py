import configparser
from modules.user_data import user_information, token_from_file
from modules.team_data import team_reserves

config = configparser.ConfigParser()
config.read('settings.ini')
application_id = config['Application']['id']
user_token = token_from_file()
team_reserves_data = team_reserves(application_id, user_token)
if 'error' in team_reserves_data:  # request a new token if an error
    user_information(application_id)
    user_token = token_from_file()
    team_reserves_data = team_reserves(application_id, user_token)  # request with a new token
print(team_reserves_data)
