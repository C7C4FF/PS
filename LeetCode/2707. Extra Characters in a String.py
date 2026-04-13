# https://leetcode.com/problems/extra-characters-in-a-string/description/
# j까지 남은 수와, i까지 남은 수를 비교해서 더 적은 것을 선택

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1

            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]
