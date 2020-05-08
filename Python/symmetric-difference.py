mint = int(input()) 

m = set([int(x) for x in input().split()])

nint = int(input())

n = set([int(y) for y in input().split()])

lis = [x for x in m.difference(n)] + [x for x in n.difference(m)]

for k in sorted(lis):
    print(k)