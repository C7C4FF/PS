# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/?envType=daily-question&envId=2026-04-12
# editorial ..

class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        dp = [[[float('inf')] * 26 for x in range(26)] for y in range(n)]
        
        for i in range(26):
            dp[0][i][ord(word[0]) - 65] = 0
            dp[0][ord(word[0]) - 65][i] = 0

        for i in range(1, n):
            curr, prev = ord(word[i]) - 65, ord(word[i-1]) - 65
            x1, y1 = divmod(prev, 6)
            x2, y2 = divmod(curr, 6)

            distance = abs(x1 - x2) + abs(y1 - y2)

            for j in range(26):
                dp[i][curr][j] = min(dp[i][curr][j], dp[i-1][prev][j] + distance)
                dp[i][j][curr] = min(dp[i][j][curr], dp[i-1][j][prev] + distance)

                if prev == j:
                    for k in range(26):
                        x3, y3 = divmod(k, 6)
                        distance_2 = abs(x2-x3) + abs(y2-y3)
                        dp[i][curr][j] = min(dp[i][curr][j], dp[i-1][k][j] + distance_2)
                        dp[i][j][curr] = min(dp[i][j][curr], dp[i-1][j][k] + distance_2)

        ans = min(min(dp[n-1][x]) for x in range(26))
        
        return ans
