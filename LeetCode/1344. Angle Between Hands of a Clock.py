# https://leetcode.com/problems/angle-between-hands-of-a-clock/?envType=daily-question&envId=2026-06-18
# 시침은 분당 0.5, 분침은 분당 6도

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_h, angle_m = 0, 0

        angle_h = hour * 30 + minutes * 0.5
        angle_m = minutes * 6

        angle = max(angle_h, angle_m) - min(angle_h, angle_m)
        
        return min(angle, 360 - angle)
