# https://leetcode.com/problems/largest-magic-square/?envType=daily-question&envId=2026-01-18

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 1

        def verify_sum(grid: List[List[int]]) -> bool:
            # 840 문제에서 썼던 함수

            std = sum(grid[0])
            length = len(grid)

            # 가로 합이 같은지 
            rows_chk = all(sum(row) == std for row in grid)
            # 세로 합이 같은지
            cols_chk = all(sum(grid[i][j] for i in range(length)) == std for j in range(length))

            # 대각선 합이 같은지
            leftdiag_chk = sum(grid[i][i] for i in range(length)) == std
            rightdiag_chk = sum(grid[i][length-1-i] for i in range(length)) == std

            return rows_chk and cols_chk and leftdiag_chk and rightdiag_chk
        
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    chk_grid = [row[j:j+k] for row in grid[i:i+k]]
                    if verify_sum(chk_grid):
                    # 바로 반환을 해줘야 가장 큰 값을 찾게 됨.
                        return k

        return ans
