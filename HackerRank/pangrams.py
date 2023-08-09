#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    
    alphaDict = dict()
    alphaStr = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in range(0,len(alphaStr)):
        alphaDict[alphaStr[letter]] = 0
    
    lowerStr = s.lower()
    
    for testLet in range(0,len(lowerStr)):
        if lowerStr[testLet] in alphaDict.keys():
            alphaDict[lowerStr[testLet]] = 1
    
    if 0 in alphaDict.values():
        return "not pangram"
    else:
        return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
