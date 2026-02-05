# https://leetcode.com/problems/transformed-array/?envType=daily-question&envId=2026-02-05
# 분기를 나누지 않아도 작동함
# return [nums[(i + v) % n] for i, v in enumerate(nums)] 이런식으로 한줄로도 가능...

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            target = nums[i] + i
            target %= n
            ans[i] = nums[target]

        return ans
