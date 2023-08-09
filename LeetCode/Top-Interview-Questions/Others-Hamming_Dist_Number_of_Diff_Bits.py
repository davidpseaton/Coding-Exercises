class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xStr = str(format(x, '032b'))
        yStr = str(format(y, '032b'))
        
        count = 0
        for i in range(0,32):
            if xStr[i] != yStr[i]:
                count += 1
        
        return count


#Faster Solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x^y
        count = 0
        while temp != 0:
            if temp%2==1:
                count+=1
            temp//=2
        return count