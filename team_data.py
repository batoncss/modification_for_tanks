from requests import get


def team_reserves(app_id, user_token):
    data = get(f"https://api.tanki.su/wot/stronghold/clanreserves/?application_id={app_id}&access_token={user_token}")
    return data.json()
