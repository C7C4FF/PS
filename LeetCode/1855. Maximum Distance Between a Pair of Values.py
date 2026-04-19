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


'''
# 정렬되어 있으면 이진탐색으로도 풀 수 있음

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n, m = len(nums1), len(nums2)
        
        for i in range(n):
            l, r = i, m-1
            farthest = i

            while l <= r:
                mid = (l+r)//2

                if nums2[mid] >= nums1[i]:
                    farthest = mid
                    l = mid+1
                else:
                    r = mid-1

            ans = max(ans, farthest-i)
        
        return ans

        
                
                
