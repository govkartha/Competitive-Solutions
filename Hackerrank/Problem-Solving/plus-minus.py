#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    print("{:.6f}\n{:.6f}\n{:.6f}".format(len([x for x in arr if x>0])/len(arr),len([x for x in arr if x<0])/len(arr),len([x for x in arr if x==0])/len(arr)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
