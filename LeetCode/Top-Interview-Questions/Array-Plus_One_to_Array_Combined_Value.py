class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        numStr = ""

        for i in range(0, len(digits)):
            numStr += str(digits[i])

        newStr = str(int(numStr) + 1)

        newList = []
        for j in range(0,len(newStr)):
            newList.append(int(newStr[j]))
            
        return newList