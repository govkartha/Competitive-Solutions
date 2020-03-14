A = set(input().split())

flag = 1

for _ in range(int(input())):
    sub = set(input().split())
    if(not(sub.issubset(A) or sub is A)):
        print("False")
        flag = 0
        break

if(flag):
    print("True")