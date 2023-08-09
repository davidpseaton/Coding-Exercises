class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s.strip('"')
        matchFlag = False
        for i in range(0,len(s)):
            for j in range(0,len(s)):
                if i != j:
                    if s[i] == s[j]:
                        matchFlag = True
                        break
                else:
                    continue
                matchFlag = False
                
            if matchFlag == False:
                return i

        return -1