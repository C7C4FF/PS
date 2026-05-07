# https://leetcode.com/problems/jump-game-ix/?envType=daily-question&envId=2026-05-07
# 큰 값이면 왼쪽으로, 작은 값이면 오른쪽으로

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n   # pre[i]: 0부터 i까지 중 가장 큰 값
        suf = [0] * n   # suf[i]: i부터 끝까지 중 가장 작은 값
        res = [0] * n   # 최종 결과

        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])

        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        res[-1] = pre[-1]

        for i in range(n - 2, -1, -1):
            if pre[i] > suf[i + 1]:
                res[i] = res[i + 1]
            else:
                res[i] = pre[i]

        return res
