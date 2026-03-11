# https://leetcode.com/problems/minimum-operations-to-equalize-array/
# 하나라도 틀린 게 있으면 처음부터 끝까지 AND 연산으로 같게 만들기
# 전부 같은 원소라면 0 반환

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if len(set(nums)) == 1:
            return 0
        else:
            return 1
