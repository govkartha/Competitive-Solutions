from collections import deque
d = deque()
for _ in range(int(input())):
    comm = input().split()

    if(comm[0] == "append"):
        d.append(comm[1])
    elif(comm[0] == "appendleft"):
        d.appendleft(comm[1])
    elif(comm[0]=="pop"):
        d.pop()
    elif(comm[0] == "popleft"):
        d.popleft()
    

print(*d)
