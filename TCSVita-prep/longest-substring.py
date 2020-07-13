def long_sbstring(val):
    i = 0
    j=0
    traversed = []
    maxlen = 0

    while(j<len(val)):
        if(not traversed.count(val[j])):
            traversed.append(val[j])
            j+=1
        else:
            maxlen = max(maxlen,len(traversed))
            i=j
            traversed = []
    maxlen = max(maxlen,len(traversed))
    return maxlen

print(long_sbstring(input("Enter the string:\n")))