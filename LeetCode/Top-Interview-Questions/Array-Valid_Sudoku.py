class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Row Valid
        for row in range(0,9):
            tempArr = ["1","2","3","4","5","6","7","8","9"]
            for col in range(0,9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in tempArr:
                    indexr = tempArr.index(board[row][col])
                    del tempArr[indexr]
                elif board[row][col] not in tempArr:
                    return False
                
        #Column Valid
        for col in range(0,9):
            tempArr = ["1","2","3","4","5","6","7","8","9"]
            for row in range(0,9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in tempArr:
                    indexc = tempArr.index(board[row][col])
                    del tempArr[indexc]
                elif board[row][col] not in tempArr:
                    return False
        
        #Square Valid
        for sqrow in range(0,9,3):
            for sqcol in range(0,9,3):
                tempArr = ["1","2","3","4","5","6","7","8","9"]
                for row in range(0,3):
                    for col in range(0,3):
                        if board[sqrow+row][sqcol+col] == ".":
                            continue
                        elif board[sqrow+row][sqcol+col] in tempArr:
                            indexs = tempArr.index(board[sqrow+row][sqcol+col])
                            del tempArr[indexs]
                        elif board[sqrow+row][sqcol+col] not in tempArr:
                            return False
                
        return True