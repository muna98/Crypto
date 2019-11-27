import requests
import pprint
import numpy as np

url = 'https://api.coinmarketcap.com/v1/ticker/'
response = requests.get(url)
currencies = response.json()

from prettytable import PrettyTable

table = PrettyTable()

for currency in currencies:
    name = currency['name']
    price = currency['price_usd']
    change_1h = currency['percent_change_1h']
    change_24h = currency['percent_change_24h']
    change_7d = currency['percent_change_7d']

    table.add_row([name,price,change_1h,change_24h,change_7d])

table.field_names = ["Name","Price","Change 1h","Change 24h","Change 7d"]
table.sortby = "Change 24h"
table.reversesort = True
print(table)

