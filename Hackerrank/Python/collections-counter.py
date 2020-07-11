from collections import Counter

n = int(input())

l = Counter([int(x) for x in input().split()])

total = 0

for _ in range(int(input())):
    size,prize = map(int,input().split())
    if(l[size]==0):
        continue
    else:
        total += prize 
        l[size]-=1
    
print(total)