import requests
from datetime import datetime


def get_line():
    params = {
        'count': '50',
        'tf': '2200000',
        'tz': '3',
        'antisports': '188',
        'mode': '4',
        'country': '1',
        'partner': '51',
        'gr': '44',
    }

    response = requests.get('https://1xstavka.ru/LineFeed/Get1x2_VZip', params=params)
    line_res = response.json()
    lst_line = []
    for id in line_res['Value']:
        league_id = id['LI']
        lst_line.append(league_id)
    return lst_line


def get_games(result):
    for game in result['Value']:
        game_id = game['I']
        champs = game['LI']
        team1 = game['O1']
        team2 = game['O2']
        tournament = game['L']
        timestamp = game['S']
        game_time = datetime.fromtimestamp(timestamp)
        coef = game['E']
        lst_coefs = []
        for i in coef:
            lst_coefs.append(i['C'])

        params = {
            'sports': '1',
            'champs': champs,
            'count': '50',
            'tf': '2200000',
            'antisports': '188',
            'mode': '4',
            'subGames': game_id,
            'country': '1',
            'partner': '51',
            'getEmpty': 'true',
            'gr': '44'
        }
        response = requests.get('https://1xstavka.ru/LineFeed/Get1x2_VZip', params=params)
        game_res = response.json()
        if len(coef) != 0:
            print(f'{tournament}\n{team1}-{team2}:\n П1-{lst_coefs[0]}, Ничья-{lst_coefs[1]}, П2-{lst_coefs[2]}\n'
                  f'{game_time}\n')
        # print(game_res)
        # get_sg(game_res, game_id)


def main():
    line = set(get_line())
    for elem in line:
        operate(elem)


def operate(id):
    params = {
        'sports': '1',
        'champs': id,
        'count': '50',
        'tf': '2200000',
        'antisports': '188',
        'mode': '4',
        'country': '1',
        'partner': '51',
        'getEmpty': 'true',
    }

    response = requests.get('https://1xstavka.ru/LineFeed/Get1x2_VZip', params=params)
    res = response.json()
    get_games(res)


if __name__ == '__main__':
    main()
