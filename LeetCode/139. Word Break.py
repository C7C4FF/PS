# https://leetcode.com/problems/word-break/description/
# j까지 만들 수 있고, s[j:i] 가 있다면 s[0:i] 까지도 만들 수 있음. dp[i] = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i): # 자르는 위치
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]
