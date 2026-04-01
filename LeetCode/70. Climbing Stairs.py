# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2, 3]

        if n <= 3:
            return dp[n-1]

        for i in range(3, n):
            dp.append(dp[i-2] + dp[i-1])

        return dp[n-1]

