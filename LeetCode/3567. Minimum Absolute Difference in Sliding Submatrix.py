# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/?envType=daily-question&envId=2026-03-20
# 한 줄 씩 처리해야 ans[i][j] 가 submatrix의 top-left 를 될 수 있음

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        m, n = len(grid), len(grid[0])

        if k == 1:
            return [[0] * n] * m

        for i in range(0, m-k+1):
            row = []

            for j in range(0, n-k+1):
                submatrix = []
                for l in range(k):
                    submatrix += grid[i+l][j:j+k]

                set_submatrix = sorted(set(submatrix))

                if len(set_submatrix) == 1:
                # 모두 같은 값이라면 0
                    row.append(0)
                else:
                    gap = float('inf')
                    for idx in range(1, len(set_submatrix)):
                        # 인접한 쌍들의 절댓값 차 구하기
                        gap = min(gap, abs(set_submatrix[idx-1] - set_submatrix[idx]))
                    row.append(gap)
                
            ans.append(row)

        return ans
