# https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        length = len(nums)
        n = length - 1

        cnt = Counter(nums)
        
        for k, v in cnt.items():
            if k > n:
                return False
            elif k == n and v != 2:
                return False
            elif k < n and v > 1:
                return False

        return True
