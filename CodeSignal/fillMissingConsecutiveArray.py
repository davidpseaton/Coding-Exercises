def solution(statues):
    sortedArray = sorted(statues)
    totalNum = 0
    for i in range(0, len(sortedArray)-1):
        subDiff = sortedArray[i+1]-sortedArray[i]
        if subDiff > 1:
            totalNum += (subDiff-1)
    
    return totalNum