if __name__ == '__main__':
    lis = []
    namelis = []
    lowm = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name,score])
    lis = sorted(lis,key=lambda x : x[1])
    
    lowm = lis[0][1]
    low2 = 0 
    trigger = 0
    for i in lis:
        current = i[1]
        if(trigger == 0 and current!=lowm):
            low2 = current
            trigger = 1
            namelis.append(i[0])
        elif(current == low2 and trigger):
            namelis.append(i[0])

    for x in sorted(namelis):
        print(x)
