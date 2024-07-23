#  https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict
n=int(input())
item_prices=OrderedDict()
for _ in range(n):
    entry=input().rsplit(' ',1)
    item=entry[0]
    price=int(entry[1])
    if item in item_prices:
        item_prices[item]+=price
    else:
        item_prices[item]=price
for item,net_price in item_prices.items():
    print(f"{item} {net_price}")
