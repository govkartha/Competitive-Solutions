from math import factorial as fact


# arg size is the size of the square grid
def getroutes(rows, cols):
    return fact((rows+cols))//(fact(rows)*fact(cols))


# for 20*20 grid
print(getroutes(20, 20))
