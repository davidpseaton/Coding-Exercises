class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        matchFlag = False
        
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                for j in range(0,len(needle)):
                    if haystack[i+j] == needle[j]:
                        matchFlag = True
                        continue
                    else:
                        matchFlag = False
                        break
            if matchFlag == True:
                return i
            
        return -1
		

#Other Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if needle in haystack:
                x = haystack.index(needle)
            else:
                x = -1
        return x