# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        '''
        (sub[0] + sub[1]) % k == sub[0] % k + sub[1] % k
        '''
        dp = [[0] * k for _ in range(k)]
        res = 0

        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])

        return res
