import requests
from data.config import link_city, API_KEY
import json



q = 'Москва'
def get_place(q: str = q, appid: str = API_KEY):
    datas = requests.get(f'{link_city}', params=locals()).json()
    lat = datas[0]['lat']
    lon = datas[0]['lon']
    return lat, lon
