n = int(input())

nlist = [x for x in input().split()]

print(all(int(x) > 0 for x in nlist) and any(x[::-1] == x for x in nlist))