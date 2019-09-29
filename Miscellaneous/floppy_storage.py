#A floppy disk shows "f" bytes free and "u" bytes used
#if you delete a file of size "o" bytes and create an new file of size "n" bytes,
# how many free bytes will the floopy disk have?
#input is f,u,o and n respectively

f = int(input())
u = int(input())
o = int(input())
n = int(input())

f += o-n

print(f)