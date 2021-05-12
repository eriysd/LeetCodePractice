class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #rotate horizontal
        totalRows = len(matrix)
        for row in range(totalRows//2):
            matrix[row], matrix[totalRows-row-1] = matrix[totalRows-row-1], matrix[row]
        
        #invert
        for row in range(totalRows):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        return matrix
