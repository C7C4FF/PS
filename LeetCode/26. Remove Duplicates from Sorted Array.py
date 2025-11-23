# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnt = list(cnt)
        nums[:len(cnt)] = cnt
        
        return len(cnt)
