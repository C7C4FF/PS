# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/?envType=daily-question&envId=2025-12-15

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        length = 0
        n = len(prices)

        for i in range(n):
            if i > 0 and prices[i-1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            ans += length

        return ans
