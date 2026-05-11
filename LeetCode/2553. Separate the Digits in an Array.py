# https://leetcode.com/problems/separate-the-digits-in-an-array/description/?envType=daily-question&envId=2026-05-11

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            ans += list(str(num))

        return [int(n) for n in ans]
