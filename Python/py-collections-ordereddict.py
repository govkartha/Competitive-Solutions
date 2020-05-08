from collections import OrderedDict

items = OrderedDict()

for _ in range(int(input())):
    lis = input().split()
    item_name,item_price = ' '.join(lis[:-1]),int(lis[-1])

    if item_name in items:
        items[item_name] +=item_price
    else:
        items[item_name] = item_price

for item in items:
    print(f"{item} {items[item]}")
