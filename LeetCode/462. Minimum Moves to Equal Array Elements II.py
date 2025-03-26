# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

# 정렬해주고, 중간값 구하기. 원래 nums 리스트와의 차이를 절댓값으로 구함
# 한번에 1씩 더하고 뺄 수 있으니, 그 차이만큼 연산 횟수가 필요
# 연산 횟수 = 리스트의 합

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        median = nums[len(nums)//2]
        gap = [abs(median - n) for n in nums]

        return sum(gap)
