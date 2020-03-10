from itertools import combinations

S,n = map(str,input().split())

S = sorted([x for x in S])

n = int(n)


for j in range(1,n+1):
    for i in combinations(S,j):
        print(''.join(i))