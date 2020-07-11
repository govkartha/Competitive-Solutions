from itertools import permutations

stri,n = map(str,input().split())

for i in permutations(sorted(list(stri)),int(n)):
    for k in i:
        print(k,end='')
    print()