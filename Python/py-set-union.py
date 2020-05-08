nint = input()

n = set(map(int,input().split()))

fint = input()

f = set(map(int,input().split()))

print(len(n.union(f)))