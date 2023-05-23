from requests import get


def team_reserves(app_id, user_token):
    data = get(f"https://api.tanki.su/wot/stronghold/clanreserves/?application_id={app_id}&access_token={user_token}").json()
    if data['status'] == 'ok':
        del data['data'][1], data['data'][2], data['data'][3]  # removing teams reserves
        return data['data']
    else:
        return data['status']
