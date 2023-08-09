class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        
        for col in range(0,width):
            tempRow = []
            for row in range(width-1,-1,-1):
                tempRow.append(matrix[row][col])
            matrix.append(tempRow)
        
        for i in range(0,width):
            del matrix[0]
        