# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/?envType=daily-question&envId=2026-04-10

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        cnt = defaultdict(list)

        for i in range(len(nums)):
            cnt[nums[i]] += [i]

        for k, v in cnt.items():
            if len(v) >= 3:
                for i in range(len(v)):
                    for j in range(i+1, len(v)):
                        for l in range(j+1, len(v)):
                            distance = abs(v[i] - v[j]) + abs(v[j] - v[l]) + abs(v[l] - v[i])
                            ans = min(ans, distance)

        if ans == float('inf'):
            return -1
        
        return ans
        
