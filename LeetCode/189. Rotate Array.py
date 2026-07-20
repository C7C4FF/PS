# https://leetcode.com/problems/rotate-array/
# 각 원소당 최대 2번까지 뒤집힐 수 있음. 시간복잡도 O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            this = nums.pop()
            nums.insert(0, this)

            k -= 1

'''
