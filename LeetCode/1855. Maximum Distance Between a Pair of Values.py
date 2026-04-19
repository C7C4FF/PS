# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/?envType=daily-question&envId=2026-04-19
# 이중for문은 TLE .. 투포인터로 풀기

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n, m = len(nums1), len(nums2)
        
        l, r = 0, 0

        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                ans = max(ans, r-l)
                r += 1

            else:
                l += 1
                if l > r:
                    r = l
        
        return ans

        
                
