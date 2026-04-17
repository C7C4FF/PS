# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/?envType=daily-question&envId=2026-04-17
# defaultdict 값의 초기값은 lambda로 설정 가능

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        seen = defaultdict(lambda: float('inf'))
        n = len(nums)

        for i in range(n):
            num = nums[i]
            reverse_num = int(str(num)[::-1])
            
            if seen[num] != float('inf'):
                ans = min(ans, i - seen[num])
            seen[reverse_num] = i
        
        return ans if ans != float('inf') else -1
