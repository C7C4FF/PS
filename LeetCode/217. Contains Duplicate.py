# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if Counter(nums).most_common()[0][1] != 1:
            return True
        else:
            return False

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(nums) != len(set(nums)))
'''
