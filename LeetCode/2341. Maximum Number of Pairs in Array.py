# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        cnt = Counter(nums)

        for k, v in cnt.items():
            q, r = divmod(v, 2)
            ans[0] += q
            ans[1] += r

        return ans
