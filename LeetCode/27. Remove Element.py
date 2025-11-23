# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
        
        def remove_under_bar():
            try:
                return nums.index("_")
            except:
                return None

        while remove_under_bar() is not None:
            nums.remove("_")
