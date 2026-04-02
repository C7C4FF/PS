# https://leetcode.com/problems/coin-change/description/
# 그리디 안 됨...
# coin 을 1개 써서 dp[i] 를 만들 수 있음. dp[i-coin] + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cnt = 0
        coins.sort(reverse=True)

        if amount == 0:
            return 0

        if len(coins) == 1 and coins[0] == 1:
            return amount

        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        




        

        
        
