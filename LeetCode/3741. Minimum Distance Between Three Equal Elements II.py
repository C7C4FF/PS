# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/?envType=daily-question&envId=2026-04-11
# 3740 이랑 동일하게 가능

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        cnt = defaultdict(list)

        for idx, num in enumerate(nums):
            cnt[num].append(idx)

            if len(cnt[num]) >= 3:
                distance = (cnt[num][-1] - cnt[num][-3]) * 2
                ans = min(ans, distance)

        if ans == float('inf'):
            return -1
        
        return ans
