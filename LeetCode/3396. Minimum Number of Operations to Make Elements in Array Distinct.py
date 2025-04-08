# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/?envType=daily-question&envId=2025-04-08
# 뒤에서부터 순회하면 가장 늦게 제거되는 중복 위치를 알 수 있음

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        
        for i in reversed(range(len(nums))):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])

        return 0


'''
# 중복이 있으면, 종류의 수는 리스트의 길이보다 작음.
# O(n^2)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lst = list(Counter(nums).keys())
        cnt = 0

        while len(lst) != len(nums):
            if len(nums) >= 3:
                nums = nums[3:]
            else:
                nums = []

            lst = list(Counter(nums).keys())
            cnt += 1

        return cnt

'''
