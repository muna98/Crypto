import requests
import pprint
import numpy as np
import decimal
decimal.getcontext()

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

    def truncate('price_usd', decimal=3):
    multiplier = 10 ** decimals
    return float('price_usd' * multiplier) / multiplier

print(coin['percent_change_24h'])
print(coin['percent_change_1h'])

from decimal import Decimal
Decimal('price_usd')




import csv
import collections
import matplotlib.pyplot as plt
TOP_CAP_TITLE = 'Top 10 market capitalization'
TOP_CAP_YLABEL = '% of total cap'
dec6 = pd.read_csv("coinmarketcap_06122017.csv")
market_cap_raw = dec6[['id', 'market_cap_usd']]
market_cap_raw.count()
cap = market_cap_raw.query('market_cap_usd > 0')
# Selecting the first 10 rows and setting the index
cap10 = cap.set_index('id') \
            .sort_values(by='market_cap_usd', ascending=False)[:10]

# Calculating market_cap_perc
cap10 = cap10.assign(market_cap_perc=
                     lambda x: x.market_cap_usd / cap.market_cap_usd.sum() * 100)

# Plotting the barplot with the title defined above
ax = cap10.plot.bar(y='market_cap_perc', title=TOP_CAP_TITLE)

# Annotating the y axis with the label defined above
_ = ax.set_ylabel(TOP_CAP_YLABEL)
