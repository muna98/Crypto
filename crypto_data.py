currency = input('Do you know what a crytocurrency is? (y/n) ?')
if currency =='y':
   cryptocurrency_name = input('What kinds of cryptocurrenies do you know?')
   print('You know {}'.format(cryptocurrency_name))
else:
    print('A cryptocurrency is a digital asset designed to work as a medium of exchange that uses strong cryptography to secure financial transactions, control the creation of additional units, and verify the transfer of assets.')





import requests
from pprint import pprint

crypto_id = input('Which currency do you want to look up?')

url = 'https://api.coinmarketcap.com/v1/ticker/'

response = requests.get(url)
print(response)

currencies = response.json()

for currency in currencies:
  print(currency['name'])
  print(currency['rank'])
  print(currency['price_usd'])
  print(currency['id'])
  print(currency['rank'])



