n,x = map(int,input().split())

lis = []
for i in range(x):
    lis.append([float(k) for k in input().split()])

for j in zip(*lis):
    print(sum(j)/x)