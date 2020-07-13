def fact(n):
    if(n == 1):
        return 1
    return n * fact(n-1)


# arg size is the size of the square grid
def getroutes(size):
    return fact(2*size)//(fact(size)**2)


# for 20*20 grid
print(getroutes(20))
