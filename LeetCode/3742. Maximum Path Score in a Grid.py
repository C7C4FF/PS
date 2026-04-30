# https://leetcode.com/problems/maximum-path-score-in-a-grid/?envType=daily-question&envId=2026-04-30

# m-1, n-1 에 도달 가능한 길이 있다면 거기가 답은 0보다는 크게 나올 것

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k+1):
                    if dp[i][j][c] == -1:
                        continue

                    if i + 1 < m:      # 아래로 이동
                        v = grid[i+1][j]
                        
                        if v == 0:      # 0 이 아닌 칸 방문시 비용 발생
                            cost = 0
                        else:
                            cost = 1
                        
                        if c + cost <= k:
                            dp[i+1][j][c + cost] = max(dp[i+1][j][c+cost], dp[i][j][c] + v)
                        
                    if j + 1 < n:
                        v = grid[i][j+1]
                        
                        if v == 0:
                            cost = 0
                        else:
                            cost = 1
                        
                        if c + cost <= k:
                            dp[i][j+1][c + cost] = max(dp[i][j+1][c+cost], dp[i][j][c] + v)

                    
        ans = max(dp[m-1][n-1])

        if ans >= 0:
            return ans
        else:
            return -1
