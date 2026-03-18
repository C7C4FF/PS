# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/?envType=daily-question&envId=2026-03-18

# 누적합을 만들면서 k 보다 작거나 같은 경우에 하나씩 세기

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] == 0:
            ans = 1
        else:
            ans = 0
        
        prefix_sum = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_sum[i][j] = grid[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
                if 0 < prefix_sum[i][j] <= k:
                    ans += 1

        return ans
                
