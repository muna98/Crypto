import requests
from pprint import pprint

url = 'https://api.coinmarketcap.com/v1/ticker/'

response = requests.get(url)
print(response)

currencies = response.json()
pprint(currencies)