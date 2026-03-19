# https://leetcode.com/problems/set-matrix-zeroes/description/
# 첫 row 와 col 에 0 이 있는지 확인 > 있다면 맨 마지막에 0으로 전부 바꿔주기
# matrix[i][j] 가 0이라면, 해당 row, col 맨 앞의 값을 0으로 만들기
# matrix를 다시 순회하면서 row, col의 맨 앞이 0이라면 해당 값을 0으로 만들기

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


# -----------
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
