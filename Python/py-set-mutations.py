na,A = int(input()),set([int(x) for x in input().split()])

for _ in range(int(input())):
    comm =input().split()

    

    if(comm[0] == 'update'):
        A.update(set([int(x) for x in input().split()]))
    elif(comm[0] == 'intersection_update'):
        A.intersection_update(set([int(x) for x in input().split()]))
    elif(comm[0] == 'difference_update'):
        A.difference_update(set([int(x) for x in input().split()]))
    elif(comm[0] == 'symmetric_difference_update'):
        A.symmetric_difference_update(set([int(x) for x in input().split()]))


print(sum(A))
