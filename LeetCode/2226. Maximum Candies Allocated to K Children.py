# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/?envType=daily-question&envId=2025-03-14
# candies[i] // mid 의 합이 k개가 되도록 하기

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ans = 0
        lo = 1
        hi = max(candies)

        while lo <= hi:
            curr = 0
            mid = (lo + hi) // 2

            for candy in candies:
                curr += candy // mid
            
            if curr >= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
