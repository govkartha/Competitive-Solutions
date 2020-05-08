from itertools import combinations_with_replacement

S,n = map(str,input().split())

S = sorted([x for x in S])

n = int(n)



for i in combinations_with_replacement(S,n):
    print(''.join(i))