from itertools import product
for i in list(product([int(x) for x in input().split()],[int(x) for x in input().split()])):
    print(i,end=' ')