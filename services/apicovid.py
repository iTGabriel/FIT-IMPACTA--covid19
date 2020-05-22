import requests

# Request na API, buscando as informações de todos os países
def todas_regioes():
    r = requests.get('https://api.covid19api.com/summary')
    return r

# Request na API, buscando as informações por país
def por_regiao(pais):
    r = requests.get(f'https://api.covid19api.com/live/country/{pais}/status/confirmed')
    return r