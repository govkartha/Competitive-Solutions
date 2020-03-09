n1 = int(input())

l1 = set([int(x) for x in input().split()])

n2 = int(input())

l2 = [int(x) for x in input().split()]

print(len(l1.symmetric_difference(l2)))