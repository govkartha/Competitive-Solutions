# Enter your code here. Read input from STDIN. Print output to STDOUT

lis = [input() for _ in range(int(input()))]
dic = dict()
print(len(set(lis)))
for i in lis:
    if i not in dic: dic[i] = 0
    dic[i] += 1
for i in dic.values():print(i,end=' ')
