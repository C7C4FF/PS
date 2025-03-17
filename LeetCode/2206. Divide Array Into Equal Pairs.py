# https://leetcode.com/problems/divide-array-into-equal-pairs/?envType=daily-question&envId=2025-03-17
# pair를 형성할 수 없으면 -> value가 홀수라면 False 반환

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v % 2 != 0:
                return False
        
        return True
