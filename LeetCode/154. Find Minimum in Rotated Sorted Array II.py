# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/?envType=daily-question&envId=2026-05-16

# 한번 순회하면서 중복을 제거하고 이진탐색 수행
# O(n) ...

class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()
        
        n = len(nums)

        l, r = 0, n-1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid+1    
            else:
                r = mid

        return nums[l]
