# https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/
# 가장 큰 값이 되려면 빼는 숫자는 제일 작은 수부터 넣어야 하고, 더하는 숫자는 가장 큰 숫자부터 넣어야 함
# 제곱으로 만들어주고 정렬한 뒤 낮은 쪽 절반은 빼고, 높은 쪽 절반은 더해줌

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [num ** 2 for num in nums]
        nums.sort()

        m = n // 2

        return sum(nums[m:]) - sum(nums[:m])
