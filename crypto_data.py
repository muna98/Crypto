<<<<<<< HEAD
import requests
import pprint
import numpy as np

currency = input('Do you know what a crytocurrency is? (y/n) ?')
if currency =='y':
   cryptocurrency_name = input('Which cryptocurrency do you know?')
   print('You know {}'.format(cryptocurrency_name))
else:
    print('A cryptocurrency is a digital asset designed to work as a medium of exchange that uses strong cryptography to secure financial transactions, control the creation of additional units, and verify the transfer of assets.')


crypto_id = input('Which currency do you want to look up?')

url = 'https://api.coinmarketcap.com/v1/ticker/'

response = requests.get(url)
print(response)

currencies = response.json()

cryptonames = []
for currency in currencies:
    cryptonames.append(currency['id'].lower())
print(cryptonames)

name_index = cryptonames.index(crypto_id.lower())
print(name_index)

coin = currencies[name_index]
print(coin)
print(coin['name'])
print(coin['rank'])
print(coin['price_usd'])
print(coin['percent_change_24h'])
print(coin['percent_change_1h'])




# Top 10 crypotocurrencies for price(in USD).
print('-' * 50)
print('Top 10 crypotocurrencies for price(in USD)')
print('-' * 50)
from operator import itemgetter

