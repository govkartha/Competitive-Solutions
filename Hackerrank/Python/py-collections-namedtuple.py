from collections import namedtuple
p,stud = int(input()),namedtuple('stud',[x for x in input().split()])
marks = 0

for _ in range(p):
    k = stud(*[x for x in input().split()])
    marks += int(k.MARKS)

print(marks/p)

#can't do in 4 lines since it reduces the readablilty