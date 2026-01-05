# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 결국 가장 낮은 수를 찾는 것

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
