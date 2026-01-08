# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/?envType=daily-question&envId=2026-01-08

# i와 j가 0일 때 처리를 제대로 해줘야 함...
# 누적합이 제일 큰 것을 찾기

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        neg = float('-inf')
        dp = [[neg] * len(nums2) for _ in range(len(nums1))]

        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]

                if i == 0 and j == 0:
                    dp[i][j] = product
                    continue
                if i == 0:
                    dp[i][j] = max(product, dp[i][j-1])
                    continue
                if j == 0:
                    dp[i][j] = max(product, dp[i-1][j])
                    continue

                temp = product
                temp = max(product, product + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                
                dp[i][j] = temp
        
        return dp[n-1][m-1]
