# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 <= prices[i] < 10^4
        minimum = 10001 # 지금까지의 최저가
        max_profit = -1

        for p in prices:
            if p < minimum: # 더 싼 날이 있으면 이 날 구매한다고 가정
                minimum = p
            
            profit = p - minimum
            if profit > max_profit: # 이익이 더 크면 갱신
                max_profit = profit
        return max_profit

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
'''
