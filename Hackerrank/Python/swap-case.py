def swap_case(s):
    ns = str()
    for i in s:
        if(i.isupper()):
            ns+= i.lower()
        elif(i.islower()):
            ns += i.upper()
        else:
            ns+= i
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)