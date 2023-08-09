#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    timeCopy = str(s)
    AM_PM = str(timeCopy[-2:])
    timeHr = int(timeCopy.split(':')[0])
    timeMin = int(timeCopy.split(':')[1])
    timeSec = int(timeCopy.split(':')[2][0:2])
    timeStr = ""
    
    if AM_PM == 'PM':
        if timeMin == 0 and timeSec == 0 and (timeHr == 12 or timeHr == 0):
            timeStr = '12:00:00'
            return timeStr
        if timeHr == 12:
            timeHr == 12
        else:
            timeHr += 12
        
		timeHrStr = str(timeHr)
        timeStr = timeHrStr + timeCopy[2:-2]
        return timeStr
    else:
        if timeHr == 12:
            timeHrStr = "00"
            timeStr = timeHrStr + timeCopy[2:-2]
            return timeStr
        if timeMin == 0 and timeSec == 0 and (timeHr == 12 or timeHr == 0):
            timeStr = '00:00:00'
            return timeStr
        
        timeStr = timeCopy[0:-2]    
    
    return timeStr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()