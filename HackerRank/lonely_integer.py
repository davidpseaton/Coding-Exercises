#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a.sort()
    curr = a[0]
    i = 1
    match = False
    while i < len(a):
        #check if next number is a match
        if curr == a[i]:
            i += 1
            match = True
            continue
        #new match
        elif curr != a[i] and match == True:
            curr = a[i]
            i += 1
            match = False
            continue
        elif curr != a[i] and match == False:
            break
        
    print(a)
    return curr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
