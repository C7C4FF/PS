# https://leetcode.com/problems/magic-squares-in-grid/description/

class Solution:
    def verify_sum(self, grid: List[List[int]]) -> bool:
        # 가로, 세로, 대각선의 합이 모두 같은지 확인
        # grid = 3x3

        std = sum(grid[0])

        # 가로 합이 같은지 
        rows_chk = all(sum(row) == std for row in grid)
        # 세로 합이 같은지
        cols_chk = all(sum(grid[i][j] for i in range(3)) == std for j in range(3))

        # 대각선 합이 같은지
        leftdiag_chk = sum(grid[i][i] for i in range(3)) == std
        rightdiag_chk = sum(grid[i][2-i] for i in range(3)) == std

        return rows_chk and cols_chk and leftdiag_chk and rightdiag_chk
    
    def verify_unique(self, grid: List[List[int]]) -> bool:
        # 9개의 수가 모두 1개씩 있는지, 1부터 9까지의 수인지 확인
        
        lst = [value for row in grid for value in row]

        if any(num > 9 for num in lst) or any(num == 0 for num in lst):
            return False
        
        return len(lst) == len(set(lst))


    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n-2):
            for j in range(m-2):
                matrix = [row[j:j+3] for row in grid[i:i+3]]
                if self.verify_sum(matrix) and self.verify_unique(matrix) and matrix[1][1] == 5:
                    ans += 1
        
        return ans

    
    
