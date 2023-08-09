class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        punct = [' ',',','.',"'",'"',':',';','!','?','#','$','%','&','^','(',')','*','+','-','=','@','`','_','~','[',']','{','}','/','\\','|','<','>']
        s = s.lower()
        for i in punct:
            if i in s:
                s = s.replace(i,'')
        
        if s == s[::-1]:
            return True
        else:
            return False