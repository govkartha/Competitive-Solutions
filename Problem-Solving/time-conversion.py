#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if(s.split(":")[-1][-2].upper() == 'P' and s.split(":")[0]!='12'):
        s = str(int(s[:2])+12) + s[2:]
    elif(s.split(":")[-1][-2].upper() == 'A' and s.split(":")[0]=='12'):
        s = "00" + s[2:]
    
    return(s[:-2])



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
