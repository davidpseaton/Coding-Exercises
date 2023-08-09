def solution(year):
    yearStr = str(year)
    if len(yearStr) > 2:
        decNum = int(yearStr[2:4])
        cenNum = int(yearStr[:-2])
    else:
        return 1
    print(cenNum, decNum)
    
    if decNum != 0:
        return cenNum + 1
    else:
        return cenNum