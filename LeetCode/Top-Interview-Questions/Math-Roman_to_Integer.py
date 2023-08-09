class Solution:
    def romanToInt(self, s: str) -> int:
        valDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        print(valDict)
        totalSum = 0
        i = 0
        while i < len(s):
            if i == len(s)-1:
                totalSum += valDict[s[i]]
                i += 1
            else:
                if s[i] == "I":
                    if s[i+1] == "V":
                        totalSum += 4
                        i += 2
                    elif s[i+1] == "X":
                        totalSum += 9
                        i += 2
                    else:
                        totalSum += valDict[s[i]]
                        i += 1
                    continue
                elif s[i] == "X":
                    if s[i+1] == "L":
                        totalSum += 40
                        i += 2
                    elif s[i+1] == "C":
                        totalSum += 90
                        i += 2
                    else:
                        totalSum += valDict[s[i]]
                        i += 1
                    continue
                elif s[i] == "C":
                    if s[i+1] == "D":
                        totalSum += 400
                        i += 2
                    elif s[i+1] == "M":
                        totalSum += 900
                        i += 2
                    else:
                        totalSum += valDict[s[i]]
                        i += 1
                    continue
                else:
                    totalSum += valDict[s[i]]
                    i += 1

        return totalSum