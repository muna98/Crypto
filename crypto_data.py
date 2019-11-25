import requests
from pprint import pprint

crypto_id = input('Which currency do you want to look up?')

url = 'https://api.coinmarketcap.com/v1/ticker/'

response = requests.get(url)
print(response)

currencies = response.json()
pprint(currencies)

print(currency['id'])
print(currency['name'])
print(currency['rank'])
print(currency['price_usd'])

