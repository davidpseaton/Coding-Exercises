class Solution:
    def isValid(self, s: str) -> bool:
        
        openList = ['(','[','{']
        closedList = [')',']','}']
        openStack = []

        for i in range(0,len(s)):
            if len(s) == 1:
                return False
            if s[i] in openList:
                openStack.append(s[i])
                continue
            if s[i] in closedList:
                if len(openStack) == 0:
                    return False
                if s[i] == closedList[openList.index(openStack[-1])]:
                    openStack.pop()
                else:
                    return False

        if len(openStack) == 0:
            return True
        else:
            return False


#Faster Solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if not stack:
                    return False
                elif c==")" and stack[-1]!="(":
                    return False
                elif c=="]" and stack[-1]!="[":
                    return False
                elif c=="}" and stack[-1]!="{":
                    return False
                stack.pop()
        return not stack        