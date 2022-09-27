# Date: September 27th, 2022 (5:29am)
# Difficulty: Medium

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in row:
                        row += [i]
                    if j not in col:
                        col += [j]
        if len(row) > 0:
            for i in range(len(row)):
                for j in range(len(matrix[0])):
                    matrix[row[i]][j] = 0
        if len(col) > 0:
            for i in range(len(col)):
                for j in range(len(matrix)):
                    matrix[j][col[i]] = 0
                    
       # Runtime: 119 ms, faster than 99.75% of Python3 online submissions for Set Matrix Zeroes.
       # Memory Usage: 14.9 MB, less than 16.82% of Python3 online submissions for Set Matrix Zeroes.             
       
