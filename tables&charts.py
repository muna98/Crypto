from prettytable import PrettyTable

table = PrettyTable()

for currency in currencies:
    name = (coin)[currency]['name']
    price = (coin)[currency]['quotes']['USD']['price']
    change_1h = currencies[currency]['quotes']['USD']['percent_change_1h']
    change_24h = currencies[currency]['quotes']['USD']['percent_change_24h']
    change_7d = currencies[currency]['quotes']['USD']['percent_change_7d']

    table.add_row([name,price,change_1h,change_24h,change_7d])

table.field_names = ["Name","Price","Change 1h","Change 24h","Change 7d"]
table.sortby = "Change 24h"
table.reversesort = True
print(table)

