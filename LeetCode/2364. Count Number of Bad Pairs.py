# https://leetcode.com/problems/count-number-of-bad-pairs/?envType=daily-question&envId=2025-02-09
# O(n^2)는 시간 초과남
# 모든 쌍은 nC2 = n*(n-1) / 2. bad pair를 직접 구하지 말고, good pair를 구하고 전체에서 빼기

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total_pair = int(len(nums)*(len(nums)-1)/2)
        gp = 0
        bp = 0

        nums_dict = {}
        
        for i in range(len(nums)):
            diff = nums[i] - i

            gp += nums_dict.get(diff, 0)
            nums_dict[diff] = nums_dict.get(diff, 0) + 1

        bp = total_pair - gp
        
        return bp
