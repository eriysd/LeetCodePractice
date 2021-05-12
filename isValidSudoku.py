#class Solution:
def isValidSudoku(self, board: List[List[str]]) -> bool:
    seen = set()
    
    for row, sublist in enumerate(board):
        for col, char in enumerate(sublist):
            if(char is not "."):
                if((char + "found in row" + str(row)) not in seen 
                   or (char + "found in col"+str(col)) not in seen 
                   or (char + "found in box"+ str(row//3) +"-"+ str(col//3)) not in seen):
                    seen.add(char + "found in row"+ str(row))
                    seen.add(char + "found in col"+ str(col))
                    seen.add(char + "found in box"+ str(row//3) +"-"+ str(col//3))
                else: return False
    return True

isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
