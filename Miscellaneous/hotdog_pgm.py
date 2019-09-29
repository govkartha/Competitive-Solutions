#Jack bought 400 hot dogs for the school picnic
#If they were contained in packages of 8 hot dogs,
#how many total packages did he buy?
#You must not use / or % to find the output

hd = 400

#pack = 8
npack = 0
#indhot = 0

#basic method
# for i in range(hd):
#     indhot +=1
#     if(indhot==8):
#         indhot = 0
#         npack+=1

#another way
for i in range(1,hd+1,8):
    npack+=1

print(npack)
