#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arrCopy = []
    tempTotal = 0
    arrMax = 0
    arrMin = 0
    initFlag = True
    for n in range(len(arr)):
        arrCopy = list(arr)
        arrCopy[n] = 0
        for m in range(len(arr)):
            tempTotal += arrCopy[m]
        if initFlag == True:
            arrMin = tempTotal
            arrMax = tempTotal
            initFlag = False
        else:
            if tempTotal >= arrMax:
                arrMax = tempTotal
            if tempTotal < arrMin:
                arrMin = tempTotal
        tempTotal = 0
        arrCopy = []

    print(arrMin, arrMax)    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
