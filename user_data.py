from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


def user_information(app_id):
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
        for_return = {"token": {"access_token": access_token, "expires_at": expires_at}, "user": {"nickname": nickname, "account_id": account_id}}
        with open("user_data.json", "w") as write_file:
            json.dump(for_return, write_file)
    else:
        return "error"
