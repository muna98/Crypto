currency = input('Do you know what a crytocurrency is? (y/n) ?')
if currency =='y':
   cryptocurrency_name = input('What kinds of cryptocurrenies do you know?')
   print('You know {}'.format(cryptocurrency_name))
else:
    print('A cryptocurrency is a digital asset designed to work as a medium of exchange that uses strong cryptography to secure financial transactions, control the creation of additional units, and verify the transfer of assets.')





import requests
from pprint import pprint

url = 'https://api.coinmarketcap.com/v1/ticker/'

response = requests.get(url)
print(response)

currencies = response.json()
pprint(currencies)

