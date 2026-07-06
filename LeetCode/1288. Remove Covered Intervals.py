# https://leetcode.com/problems/remove-covered-intervals/?envType=daily-question&envId=2026-07-06
# 정렬한다음 비교해주기

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        end = 0

        for s, e in intervals:
            if e > end:
                ans += 1
                end = e
        
        return ans
