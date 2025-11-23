# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(2)]
        res = 0

        for num in nums:
            num %= 2
            for prev in range(2):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])

        return res
