# https://leetcode.com/problems/longest-balanced-subarray-i/?envType=daily-question&envId=2026-02-10
# 매번 리스트를 슬라이스 (subarray = nums[l:r]) 하면 TLE
# 서브어레이를 전부 순회하되, distinct 홀짝의 수만 세기

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for l in range(n):
            cnt = defaultdict(int)
            odd, even = 0, 0

            for r in range(l, n):
                num = nums[r]

                if cnt[num] == 0:
                    if num % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                cnt[num] += 1
                
                if odd == even:
                    ans = max(ans, r-l+1)

        return ans
