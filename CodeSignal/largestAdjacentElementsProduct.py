def solution(inputArray):
    newSum = 0
    oldSum = 0
    topSum = 0
    for i in range(0,len(inputArray)-1):

        newSum = inputArray[i] * inputArray[i+1]
          
        if newSum < 0 and i == 0:
            topSum = newSum
            
        if newSum > oldSum:
            if newSum > topSum:
                topSum = newSum
        
        oldSum = newSum
    
    return topSum