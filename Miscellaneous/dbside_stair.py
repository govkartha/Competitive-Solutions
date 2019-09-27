#prints a pattern similar two this if input is 5
#            * *
#            * *
#          * * * *
#          * * * *
#        * * * * * *
#        * * * * * *
#      * * * * * * * * 
#      * * * * * * * * 
#    * * * * * * * * * * 
#    * * * * * * * * * *
#
#the input taken is a number
#the output is the the pattern(stairs) where the number of stairs is double the input

n = int(input())

for i in range(2,2*n+1,2):
    print((i*'* ').center(4*n," "))
    print((i*'* ').center(4*n," "))
