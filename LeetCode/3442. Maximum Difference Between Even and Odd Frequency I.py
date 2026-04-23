# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/
# 홀수는 가장 큰 값, 짝수는 가장 작은 값 구하기

class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)

        odd, even = [], []

        for v in cnt.values():
            if v % 2 == 0:
                heapq.heappush(even, v)
            else:
                heapq.heappush(odd, -v)

        a1 = -heapq.heappop(odd)
        a2 = heapq.heappop(even)
        
        return a1 - a2
