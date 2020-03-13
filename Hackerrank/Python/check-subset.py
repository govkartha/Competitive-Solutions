T = int(input())

for _ in range(T):
    n1 = int(input())
    nlist1 = set([int(x) for x in input().split()])

    n2 = int(input())
    nlist2= set([int(x) for x in input().split()])

    if(nlist1.issubset(nlist2)):
        print("True")
    else:
        print("False")
