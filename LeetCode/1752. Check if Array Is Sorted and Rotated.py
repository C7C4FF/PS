# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2025-02-02
# 제대로 돌았다면, original[i] = nums[i + x % original.length]
# x를 전부 비교하고, 정렬된 거랑 동일한 게 있는지 확인하기.

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        original = sorted(nums)
        
        ans = [[] for _ in range(n)]

        for x in range(n):
            for j in range(n):
                ans[j].append(nums[(j+x) % n])
        
        for lst in ans:
            if lst == original:
                return True
        
        return False
