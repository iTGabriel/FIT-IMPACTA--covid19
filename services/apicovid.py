import requests

def todas_regioes():
    r = requests.get('https://api.covid19api.com/summary')
    return r

def por_regiao(regiao):
    r = requests.get(f'https://api.covid19api.com/live/country/{regiao}/status/confirmed')
    return r