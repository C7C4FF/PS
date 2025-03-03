# https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=daily-question&envId=2025-03-03

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        same = []
        more = []

        for e in nums:
            if e == pivot:
                same.append(e)
            elif e < pivot:
                less.append(e)
            elif e > pivot:
                more.append(e)

        return less + same + more
