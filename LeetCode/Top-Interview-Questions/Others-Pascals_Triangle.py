class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            pascal = [[1]]
        else:
            pascal = [[1],[1,1]]
            for i in range(2,numRows):
                pascal.append([])
                tempList = []
                tempList.append(1)
                for j in range(0,i-1):
                    tempList.append(pascal[i-1][j] + pascal[i-1][j+1])
                tempList.append(1)
                pascal[i] = tempList
                
        return pascal


#Faster Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            if not triangle:
                triangle.append([1])
            else:
                length = len(triangle[-1])+1
                pre_lvl = triangle[-1]
                row_nums = []
                for i in range(length):
                    if i ==0 or i == length-1:
                        row_nums.append(1)
                    else:
                        row_nums.append(pre_lvl[i-1] + pre_lvl[i])
                triangle.append(row_nums)
        return triangle