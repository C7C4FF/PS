# https://leetcode.com/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2026-04-14
# [pos, limit, pos, limit, ...] 으로 관리하는 것보다, limit 만큼 복제해주기
# 역순으로 순회해서 중복 사용을 없애야 함

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        robot.sort()
        factory.sort()

        fac = []
        for pos, limit in factory:
            fac.extend([pos] * limit)

        dp = [0] + [float('inf')] * n
        
        for f in fac:
            for i in range(n, 0, -1):
                dp[i] = min(dp[i], dp[i-1] + abs(robot[i-1] - f))

        return dp[n]
