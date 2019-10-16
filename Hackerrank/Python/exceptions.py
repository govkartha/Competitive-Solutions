for i in range(int(input())):
    l = input().split()
    try:
        x = int(l[0])//int(l[1])
        print(x)
    except ZeroDivisionError as er:
        print('Error Code:',er)
    except ValueError as e:
        print("Error Code:",e)