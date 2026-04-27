# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        timePoints.sort()
        gap = float('inf')
        
        if n != len(set(timePoints)):
            return 0

        # 전체 시간 = 시간 * 60 + 분 
        def get_minutes(time: str) -> int:
            h, m = map(int, time.split(':'))
            return h * 60 + m

        for i in range(1, n):
            prev = get_minutes(timePoints[i-1])
            now = get_minutes(timePoints[i])

            gap = min(gap, now - prev)  # 정렬했기에 now 가 항상 더 큼
        
        first = get_minutes(timePoints[0])  # 인접한 쌍만 계산했기에 맨 처음과 맨 마지막을 비교해야 함
        last = get_minutes(timePoints[-1])

        gap = min(gap, 1440 - last + first) 
        
        return gap
