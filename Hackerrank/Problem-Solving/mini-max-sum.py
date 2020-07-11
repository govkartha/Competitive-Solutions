#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumlist = [sum(arr[:i] + arr[i+1:]) for i in range(len(arr)) ]
    print("{} {}".format(min(sumlist),max(sumlist)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
