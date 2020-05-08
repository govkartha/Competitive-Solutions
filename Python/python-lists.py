if __name__ == '__main__':
    nlist = []

    def lister(lis):
        global nlist

        if(lis[0] == 'insert'):
            nlist.insert(int(lis[1]), int(lis[2]))
        elif(lis[0] == 'print'):
            print(nlist)
        elif(lis[0] == 'remove'):
            nlist.remove(int(lis[1]))
        elif(lis[0] == 'append'):
            nlist.append(int(lis[1]))
        elif(lis[0] == 'sort'):
            nlist = sorted(nlist)
        elif(lis[0] == 'pop'):
            nlist.pop()
        elif(lis[0] == 'reverse'):
            nlist = nlist[::-1]

    n = int(input())
    for i in range(n):
        lister(input().split())
