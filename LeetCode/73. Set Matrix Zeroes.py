# https://leetcode.com/problems/set-matrix-zeroes/description/
# 0을 먼저 체크해야 함 > 아니면 2중 for문을 돌면서 0이 계속 번져버림

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        pos_row = []
        pos_col = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pos_row.append(i)
                    pos_col.append(j)
        
        for x in pos_row:
            for j in range(n):
                matrix[x][j] = 0
        
        for y in pos_col:
            for i in range(m):
                matrix[i][y] = 0
