# https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2026-03-04
# 1이 총 몇번 나오는지 계산하고, row 에서도 col 에서도 1번씩만 등장했으면 집계

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0

        m = len(mat)
        n = len(mat[0])

        row = [0] * m
        col = [0] * n

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    row[r] += 1
                    col[c] += 1

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    if row[r] == col[c] == 1:
                        ans += 1
        
        return ans
