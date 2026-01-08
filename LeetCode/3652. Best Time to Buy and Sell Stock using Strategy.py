# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/?envType=daily-question&envId=2025-12-18
# [-1, 0, 1] = [구매, x, 팔기]
# at most one modification .. 0회 or 1회

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + prices[i-1] * strategy[i-1]
        
        base = prefix_sum[n]
        modify = sum(prices[k//2:k]) # 앞쪽은 영향이 없고, 뒤는 전부 팔게 됨

        ans = base # 수정이 없는 경우
        ans = max(ans, base - (prefix_sum[k] - prefix_sum[0]) + modify) # 첫 윈도우
        
        for i in range(1, n+1-k):
            # 수익 = 기본 - (원래 구간 수익) + (수정 구간 수익)
            # 슬라이딩 윈도우로 뒤 절반에 새로 들어온 값을 더하고, 밀려난 값 빼기
            modify += prices[i+k-1] - prices[i+(k//2)-1]
            profit = base - (prefix_sum[i+k] - prefix_sum[i]) + modify

            ans = max(ans, profit)
        
        return ans
