n = int(input())
s = set(map(int, input().split()))

def controller(comm):

    if(comm[0] == 'pop'):
        s.pop()
    elif(comm[0] == 'remove'):
        s.remove(int(comm[1]))
    elif(comm[0] == 'discard'):
        s.discard(int(comm[1]))

N = int(input())

for _ in range(N):
    controller(input().split())

print(sum(s))