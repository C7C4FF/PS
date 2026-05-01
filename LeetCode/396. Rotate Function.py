# https://leetcode.com/problems/rotate-function/description/?envType=daily-question&envId=2026-05-01

# F(0) = 0 * nums[0] + 1 * nums[1] + 2 * nums[2] + ... + n-1 * nums[n-1]
# F(1) = 0 * nums[n-1] + 1 * nums[0] + 2 * nums[1] + 3 * nums[2] + ... + n-1 * nums[n-2]
# F(2) = 0 * nums[n-2] + 1 * nums[n-1] + 2 * nums[0] + 3 * nums[1] + ... + n-1 * nums[n-3]
# F(1) - F(0) = 1 * nums[0] + 1 * nums[1] + ... + 1-n * nums[n-1] = sum(nums) - n * nums[n-1]
# F(2) - F(1) = 1 * nums[0] + ... + 1-n * nums[n-2] + 1 * nums[n-1] = sum(nums) - n * nums[n-2]
# F(k) - F(k-1) = sum(nums) - n * nums[n-1-k]

# F(k) = F(k-1) - sum(nums) - n * nums[n-1-k]

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        start = 0
        for i in range(n):
            start += i * nums[i]

        dp = [[0] for _ in range(n)]
        dp[0] = start

        for i in range(1, n):
            dp[i] = dp[i-1] + total - n * nums[n-i]

        return max(dp)
