#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binStr = bin(n).split('b')[1]

    for z in range(0, 32-len(binStr)):
        binStr = "0" + binStr
    
    flipStr = ""

    for i in range(0, len(binStr)):
        if binStr[i] == '0':
            flipStr = flipStr + '1'
        elif binStr[i] == '1':
            flipStr = flipStr + '0'
    
    return int(flipStr, 2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
