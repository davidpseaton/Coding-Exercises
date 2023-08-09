class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tempStr = ""
        for i in range(0,len(s)):
            tempStr += s[i]
        revStr = tempStr[::-1]
 
        for j in range(0,len(revStr)):
            s[j] = revStr[j]