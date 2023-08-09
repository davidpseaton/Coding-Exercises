class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sDict = {}
        tDict = {}
        
        for i in range(0,len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
        
        for j in range(0,len(t)):
            if t[j] in tDict:
                tDict[t[j]] += 1
            else:
                tDict[t[j]] = 1
        
        if sDict == tDict:
            return True
        else:
            return False