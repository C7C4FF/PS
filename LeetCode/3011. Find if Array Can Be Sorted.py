# https://leetcode.com/problems/find-if-array-can-be-sorted/
# 인접한 수들의 비트가 같은지 확인하고 거기까지 정렬

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            ones = bin(nums[i])[2:].count('1')

            while j < n and bin(nums[j])[2:].count('1') == ones:
                j += 1
            
            nums[i:j] = sorted(nums[i:j])
            i = j

        return nums == sorted(nums)

            
            
        
