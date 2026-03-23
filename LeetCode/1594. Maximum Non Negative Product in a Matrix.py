# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/?envType=daily-question&envId=2026-03-23

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[grid[0][0], grid[0][0]] for _ in range(n)] for _ in range(m)] # [min, max]

        for i in range(m):
            for j in range(n):
                target = grid[i][j]

                if i == 0 and j == 0:
                # dp의 첫 값을 grid[0][0] 으로 초기화해줬기에 건너뛰기
                    continue
                
                if i > 0 and j > 0:
                    dp[i][j][0] = min(target * dp[i][j-1][0], target * dp[i-1][j][0], target * dp[i][j-1][1], target * dp[i-1][j][1])
                    dp[i][j][1] = max(target * dp[i][j-1][0], target * dp[i-1][j][0], target * dp[i][j-1][1], target * dp[i-1][j][1])
                
                elif i > 0 and j == 0:
                # 첫번째 col
                    dp[i][j][0] = min(target * dp[i-1][j][0], target * dp[i-1][j][1])
                    dp[i][j][1] = max(target * dp[i-1][j][0], target * dp[i-1][j][1])
                
                elif j > 0 and i == 0:
                # 첫번째 row
                    dp[i][j][0] = min(target * dp[i][j-1][0], target * dp[i][j-1][1])
                    dp[i][j][1] = max(target * dp[i][j-1][0], target * dp[i][j-1][1])


        return -1 if dp[m-1][n-1][1] < 0 else (dp[m-1][n-1][1] % MOD)
        
        
    
