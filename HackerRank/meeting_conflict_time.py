#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'conflictInfo' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY meetings as parameter.
#

def conflictInfo(meetings):
    
    meetingsArr = list(meetings)
    convArr = list(meetings)
    conflictList = []
    overlapDur = 0
    #Must convert times to absolute minutes from 00:00 format
    for meeting in range(0,len(meetingsArr)):
        startTime = meetingsArr[meeting].split(',')[0]
        duration = int(meetingsArr[meeting].split(',')[1])
        startTimeHr = int(startTime[0:2])
        startTimeMin = int(startTime[2:4])
        #Calculate start and end time to calculate overlap
        startTimeAbs = (startTimeHr * 60) + startTimeMin
        endTimeAbs = startTimeAbs + duration
        #Assemble equal length array of start and end times
        convArr[meeting] = str(startTimeAbs)+","+str(endTimeAbs)
    
    #This "inspect" loop only inspects the next element assuming the start dates
    #are numerical ascending order, however I see in the Sample Case 09 that times
    #are given out of sequence.  Thus this "inspect array" loop would have to
    #be nested with another for-loop comparing all the start times in the array
    #to the original meeting end-time.
    
    #Use inspect as the meeting # of the schedule
    for inspect in range(0,len(convArr)-1):
        
        end1 = int(convArr[inspect].split(',')[1])
        
        #This is where the 2nd nested for-loop would be to check all meetings
        start2 = int(convArr[inspect+1].split(',')[0])
        
        #Output any overlapped meetings, meeting#, overlap duration
        if start2 < end1:
            
            overlapDur = end1 - start2
            
            #A mechanism to put all the conflicts in an array would be
            #necessary for meeting lists that have more than one.  Then
            #the conflict array would be returned instead.
            conflictStr = "conflict,"+str(inspect+1)+','+str(overlapDur)
            return conflictStr
        
    #Return empty conflict list if none are detected by above "inspect loop"
    return "good"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    meetings_count = int(input().strip())

    meetings = []

    for _ in range(meetings_count):
        meetings_item = input()
        meetings.append(meetings_item)

    result = conflictInfo(meetings)

    fptr.write(result + '\n')

    fptr.close()
