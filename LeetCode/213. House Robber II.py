# https://leetcode.com/problems/house-robber-ii/
# 원형으로 이어져 있으면, 맨 처음과 맨 마지막은 동시에 훔칠 수 없음.
# 맨 처음을 뺀 리스트와, 맨 마지막을 뺀 리스트를 두 가지로 나눠서 그 중 큰 결과를 반환

class Solution:
    def dp(self, lst: List[int]) -> int:
        n = len(lst)
        dp = [0] * n
        dp[0] = lst[0]

        if n > 1:
            dp[1] = max(lst[0], lst[1])
    
        for i in range(2, n):
            dp[i] = max(dp[i-2] + lst[i], dp[i-1])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            not_last = self.dp(nums[:n-1])
            not_first = self.dp(nums[1:])

        return max(not_last, not_first)
