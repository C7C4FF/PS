# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/?envType=daily-question&envId=2026-01-10

# 아스키 코드를 구하는 ord('a'), 반대로 아스키 코드 값에 해당하는 문자를 구하는 chr(97)
# 삭제되는 합이 가장 작다는 것 = 남아있는 글자의 아스키 합이 가장 크다는 것

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        substring = dp[n][m]
        return sum(map(ord, s1)) + sum(map(ord, s2)) - 2 * substring
