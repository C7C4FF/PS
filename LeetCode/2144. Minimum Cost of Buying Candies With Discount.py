# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/?envType=daily-question&envId=2026-06-01
# 3번째마다 건너뛰기

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()

        ans = 0
        cnt = 0
        for i in range(len(cost)-1, -1, -1):
            if cnt == 2:
                cnt = 0
                continue
            else:a
                ans += cost[i]
                cnt += 1

        return ans
