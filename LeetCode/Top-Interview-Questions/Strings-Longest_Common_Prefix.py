class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        try:
            resultStr = ""
            letter = 0
            
            while True:
                for words in range(0,len(strs)-1):
                    if strs[words][letter] == strs[words+1][letter]:
                        continue
                    else:
                        return resultStr
                resultStr += strs[0][letter]
                letter += 1
        
        except IndexError:
            return resultStr