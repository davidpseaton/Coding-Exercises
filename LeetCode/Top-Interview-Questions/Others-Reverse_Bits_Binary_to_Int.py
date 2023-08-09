class Solution:
    def reverseBits(self, n: int) -> int:
        
        binStr = str(format(n, '032b'))
        revStr = binStr[::-1]

        return int(revStr,2)


#Faster Solution
class Solution:
    def reverseBits(self, n: int) -> int: 
        return int("{0:b}".format(n).zfill(32)[::-1], 2)
		

class Solution:
    def reverseBits(self, n: int) -> int:
        a = str(bin(n).split('b')[-1]).zfill(32)
        b = a[::-1]
        return int(b,2)
