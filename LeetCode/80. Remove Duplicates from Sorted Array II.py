# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/ 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            j = i
            while j < n and nums[j] == x:
                j += 1
            keep = min(2, j - i)
            for _ in range(keep):
                nums[w] = x
                w += 1
            i = j
        del nums[w:]
