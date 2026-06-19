# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=daily-question&envId=2026-06-19
# 초기값 0을 확인하기

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        now = 0

        for h in gain:
            now += h
            altitude.append(now)
        
        return max(altitude)
