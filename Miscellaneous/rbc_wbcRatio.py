#one cubic millimeter of blood has  5,000,000 rbc and 8000 wbc
#find the ratio between them
#it should be an integer

def HCF(num1,num2):
    if(num2==0):
        return num1
    else:
        return HCF(num1,num1%num2) if(num1<num2) else HCF(num2,num2%num1)

rbc = 5000000
wbc = 8000

factor = HCF(rbc,wbc)

print("{}:{}".format(rbc//factor,wbc//factor))
