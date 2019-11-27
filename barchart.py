# Creating a barchart
import matplotlib.pyplot as plt
import numpy as np

url = 'https://api.coinmarketcap.com/v1/ticker/'
response = requests.get(url)
currencies = response.json()

cryptonames = []
for currency in currencies:
    cryptonames.append(currency['id'].lower()

plt.bar(labels, values)

plot = plt

plt.figure()
plt.bar(labels, values)
plt.ylabel('Price in USD')
plt.xlabel('Currency name')
plt.title('Top 5 cryptocurrencies and their prices in USD')
plt.savefig(cryptocurrency_name)
plt.show
