# https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=daily-question&envId=2025-03-03
# https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=daily-question&envId=2026-06-08

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        same = []
        greater = []

        for e in nums:
            if e == pivot:
                same.append(e)
            elif e < pivot:
                less.append(e)
            else:
                greater.append(e)

        return less + same + greater
