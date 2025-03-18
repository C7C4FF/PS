# https://leetcode.com/problems/house-robber/
# dp[0] 는 해당 칸까지 얻을 수 있는 최대치.
# 2칸 떨어져있는 것 + 현재 or 그 이전 것 중 큰 쪽을 택하기

# M(k) = money at the kth house
# P(0) = 0
# P(1) = M(1)
# P(k) = max(P(k−2) + M(k), P(k−1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        if n > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]
