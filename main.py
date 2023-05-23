from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests import get
import configparser


def user_data(app_id):
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=chrome_options)
    url = f"https://api.tanki.su/wot/auth/login/?application_id={app_id}"
    driver.get(url)
    while True:
        if "status=" in driver.current_url:
            break
    if 'ok' in driver.current_url:
        data = driver.current_url
        access_token = data[data.find('access_token=') + 13:data.find("&nickname=")]
        nickname = data[data.find('nickname=') + 9:data.find("&account_id")]
        account_id = data[data.find("account_id=") + 11:data.find("&expires_at")]
        expires_at = data[data.find("expires_at=") + 11:]
        for_return = {"access_token": access_token, "nickname": nickname, "account_id": account_id,
                      "expires_at": expires_at}
        return for_return
    else:
        return "error"


def clans_reserves(app_id, token):
    data = get(f"https://api.tanki.su/wot/stronghold/clanreserves/?application_id={app_id}&access_token={access_token}")
    return data.json()


config = configparser.ConfigParser()
config.read('settings.ini')
application_id = config['Application']['id']
file = open('user_data.txt', "w")
file.write(str(user_data(application_id)))
