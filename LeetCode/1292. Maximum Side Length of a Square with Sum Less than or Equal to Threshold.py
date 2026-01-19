# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/?envType=daily-question&envId=2026-01-19
# prefixsum[i+1][j+1] = 0,0 ~ i,j 까지의 합

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pfs = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # 위쪽까지의 합 + 왼쪽까지의 합 - 중복 + 현재 값
                pfs[i][j] = pfs[i-1][j] + pfs[i][j-1] - pfs[i-1][j-1] + mat[i-1][j-1]
        
        # 사각형의 합 = 오른쪽 아래 - 왼쪽 아래 - 오른쪽 위 + 왼쪽 위
        def square_sum(x1, y1, x2, y2):
            return pfs[x2][y2] - pfs[x1][y2] - pfs[x2][y1] + pfs[x1][y1]

        def find_square(side, threshold):
            if side == 0:
                return True

            for x1 in range(0, m - side + 1):
                x2 = x1 + side

                for y1 in range(0, n - side + 1):
                    y2 = y1 + side

                    if square_sum(x1, y1, x2, y2) <= threshold:
                        return True
            
            return False

        lo, hi = 0, min(m, n)
        while lo <= hi:
            mid = (lo + hi) // 2
            if find_square(mid, threshold):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi



