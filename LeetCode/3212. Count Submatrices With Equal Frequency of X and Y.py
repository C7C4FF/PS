# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/?envType=daily-question&envId=2026-03-19
# X를 1로, Y를 -1로, .을 0으로 변환 후 prefix_sum 사용해서 매트릭스 만들기
# 최소 1개 이상의 X이 존재해야 함

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        prefix_sum = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]
        ans = 0

        for row in grid:
            for i in range(n):
                if row[i] == "X": row[i] = 1
                elif row[i] == "Y": row[i] = -1
                else: row[i] = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_sum[i][j][0] = (
                    grid[i-1][j-1]
                    + prefix_sum[i-1][j][0]
                    + prefix_sum[i][j-1][0]
                    - prefix_sum[i-1][j-1][0]
                )

                is_one = 1 if grid[i-1][j-1] == 1 else 0

                prefix_sum[i][j][1] = (
                    is_one
                    + prefix_sum[i-1][j][1]
                    + prefix_sum[i][j-1][1]
                    - prefix_sum[i-1][j-1][1]
                )

                if prefix_sum[i][j][0] == 0 and prefix_sum[i][j][1] > 0:
                    ans += 1

        return ans
