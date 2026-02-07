# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
# 총 갯수에서 겹치는 부분을 빼기 > 나머지는 개당 1개의 화살이 필요

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        points.sort(key=lambda x:x[1])

        finished = points[0][1]

        for i in range(1, n):
            s, e = points[i][0], points[i][1]

            if s <= finished:
                ans += 1
            else:
                finished = e

        return n - ans
