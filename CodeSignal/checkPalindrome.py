def solution(inputString):
    length = len(inputString)
    halfway = int(length/2)
    evenOdd = len(inputString) % 2

    if length == 1:
        return True
    else:      
        firstHalf = inputString[0:halfway]
        secondHalf = inputString[length:halfway-1+evenOdd:-1]

    if firstHalf == secondHalf:
        return True
    else:
        return False