cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    lis = []
    if(n==1):
        lis +=[0]
    elif(n!=0):
        lis += [0,1]
        for i in range(2,n):
            lis.append(lis[-1]+lis[-2])
    return lis
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))