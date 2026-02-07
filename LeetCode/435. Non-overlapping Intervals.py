# https://leetcode.com/problems/non-overlapping-intervals/description/
# 최소 제거 = 겹치지 않는 구간을 최대한 많이 고르기
# 짧게 끝나는 구간들을 고르는 것이 가장 수를 늘릴 수 있음

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        n = len(intervals)
        intervals.sort(key=lambda x:x[1])

        finished = intervals[0][1]

        for i in range(1, n):
            s, e = intervals[i][0], intervals[i][1]

            if s < finished:
                ans += 1
            else:
                finished = e

        return ans
