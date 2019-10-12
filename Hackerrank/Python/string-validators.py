if __name__ == '__main__':
    s = input()
    
    for func in [str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]:
        print(any(func(c) for c in s))

#The any() method returns
#  True if any element of an iterable is True.
#  If not, any() returns False. 