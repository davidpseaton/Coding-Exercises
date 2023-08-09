class Solution:
    def reverse(self, x: int) -> int:
        numStr = str(x)
        revStr = numStr[::-1]
        if revStr[-1] == "-":
            revStr = "-" + revStr[0:-1]
        revInt = int(revStr)
        if revInt < -2**31 or revInt > ((2**31) - 1):
            return 0
        else:
            return revInt