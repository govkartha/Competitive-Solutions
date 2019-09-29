# a bus carries 1,200,000 people each day
# how many people does the bus carry each day
# don't use *,/ operator,bitwise operator or loop
import time

def passen(daypass,iter=1):
    if(iter==365):
        return daypass
    
    return daypass+passen(daypass,iter+1)

print(passen(1200000))