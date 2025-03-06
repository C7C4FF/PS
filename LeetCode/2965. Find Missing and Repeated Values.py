# https://leetcode.com/problems/find-missing-and-repeated-values/?envType=daily-question&envId=2025-03-06
# 1부터 len(gist)^2 까지 순회하면서 두번 나온 수는 ans[0], 안 나온 수는 ans[1]에 할당


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = Counter()
        for lst in grid:
            a += Counter(lst)

        ans = [0, 0]
        for i in range(1, len(grid)**2+1):
            if not a[i]:
                ans[1] = i
            if a[i] == 2:
                ans[0] = i

        return ans
