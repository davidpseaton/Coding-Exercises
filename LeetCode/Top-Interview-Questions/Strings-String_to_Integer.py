class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()

        if len(s) == 0:
            return 0

        numInt = 0
        i = 0

        isNeg = s[0] == '-'
        isPos = s[0] == '+'

        if isNeg or isPos:
            i += 1

        while i < len(s) and '0' <= s[i] <= '9':
            numInt = numInt * 10 + (ord(s[i]) - ord('0'))
            i += 1

        if isNeg:
            numInt = -numInt

        if numInt < -2**31:
            return -2**31
        if numInt > 2**31 - 1:
            return 2**31 - 1
        
        return numInt



class Solution:
    def myAtoi(self, s: str) -> int:
        
        numSet = ['0','1','2','3','4','5','6','7','8','9']
        punctSet = ['+','.','-']
        testStr = s.replace(" ", "")

        i = 0
        l = len(testStr)
        
        if (len(testStr) == 0):
            return 0
        elif (len(testStr) == 1) and (testStr[0] not in numSet):
            return 0

        elif ((testStr[0] == '-') or (testStr[0] == "+") or (testStr[0] == '0')) and (testStr[1] not in numSet):
            return 0
        else:
            if testStr[0].isalpha():
                return 0
            leadZeroVal = True
            while i < l-1:
                print("length",l)
                print("iter", i)
                print(testStr)
                
                if leadZeroVal == True and testStr[i] == '0':
                    testStr = testStr[i+1:]
                    #i -= 1
                    l -= 1
                else:
                    if ((testStr[i] not in numSet) and (testStr[i] not in punctSet)):
 
                        testStr = testStr.replace(testStr[i], "")
                        print(testStr)
                        l -= 1
                        i -= 1
                    else:
                        leadZeroVal = False
                        i += 1
        
        testStr = testStr.replace('+','')
        
        print(testStr)
        testInt = int(float(testStr))
        
        if testInt < -2**31:
            return -2**31
        if testInt > 2**31 - 1:
            return 2**31 - 1
        
        return testInt