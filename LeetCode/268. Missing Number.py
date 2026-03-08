# https://leetcode.com/problems/missing-number/
# 주어진 nums의 총 합을 구하고, 원래 모든 원소가 있었을 때의 합을 구한다
# 원래의 총합에서 nums의 총 합을 빼면 빠진 수를 구할 수 있음


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)

        original = n * (n+1) // 2

        return original - total
