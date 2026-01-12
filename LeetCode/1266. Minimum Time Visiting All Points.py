# https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2026-01-12
# 기울기 맞추기 > 두 좌표의 차이 중 더 작은 쪽으로 계산

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        for i in range(1, n):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            gap_x, gap_y = abs(x1 - x2), abs(y1 - y2)
            gap = abs(gap_x - gap_y)

            ans += gap # 대각선 이동을 위한 기울기 맞춰주기
            
            ans += min(abs(x1 - x2), abs(y1 - y2))

        return ans 
            
