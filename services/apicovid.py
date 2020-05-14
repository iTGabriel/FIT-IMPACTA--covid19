import requests

def todas_regioes():
    r = requests.get('https://api.covid19api.com/summary')
    return [r, r.status_code]