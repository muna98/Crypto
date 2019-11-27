import requests
from pprint import pprint

url = 'https://api.coinmarketcap.com/v1/ticker/'
response = requests.get(url)
currencies = response.json()
pprint(currencies)

# Top 10 crypotocurrencies for price(in USD).
print('-' * 50)
print('Top 10 crypotocurrencies for price(in USD)')
print('-' * 50)
from operator import itemgetter

top10_price = sorted(currencies, key=itemgetter('price_usd'), reverse=True)
for price in top10_price[:10]:
    print(price['name'])
    print(price['price_usd'])

# Top 10 crypotocurrencies for 24h_volume_usd .
print('-' * 50)
print('Top 10 crypotocurrencies for 24h_volume_usd')
print('-' * 50)
from operator import itemgetter

top10_volume = sorted(currencies, key=itemgetter('24h_volume_usd'), reverse=True)
for price in top10_volume[:10]:
    print(price['name'])
    print(price['24h_volume_usd'])

# Top 10 crypotocurrencies for market cap.
print('-' * 50)
print('Top 10 crypotocurrencies for market cap')
print('-' * 50)
from operator import itemgetter

top10_marketcap = sorted(currencies, key=itemgetter('market_cap_usd'), reverse=True)
for price in top10_marketcap[:10]:
    print(price['name'])
    print(price['market_cap_usd'])

# Cryptoprice converter(to USD) .
currency_name = str(input('Which currency do you want to look up?'))
for d in currencies:
    if d['name'] == currency_name:
        p = float((d['price_usd']))
        print('The current price of', currency_name, 'coins in USD is', p)

n = float(input('How many coins you have?'))


def usd_converter(n, p):
    print(n * p)


usd_converter(n, p)



