# https://leetcode.com/problems/greatest-sum-divisible-by-three/?envType=daily-question&envId=2025-11-23
# 총 합의 나머지가 1이라면 > 나머지가 1인 수 1개 제거 or 나머지가 2인 수 2개 제거
# 총 합의 나머지가 2라면 > 나머지가 2인 수 1개 제거 or 나머지가 1인 수 2개 제거

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod1 = []
        mod2 = []
        total = sum(nums)

        for num in nums:
            if num % 3 == 1:
                heapq.heappush(mod1, num)
            elif num % 3 == 2:
                heapq.heappush(mod2, num)
        
        subtrahend = 10**4+1 

        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            if len(mod1) >= 1:
                subtrahend = min(subtrahend, mod1[0])
            if len(mod2) >= 2:
                a = heapq.heappop(mod2)
                b = heapq.heappop(mod2)
                subtrahend = min(subtrahend, a+b)
        else:
            if len(mod1) >= 2:
                a = heapq.heappop(mod1)
                b = heapq.heappop(mod1)
                subtrahend = min(subtrahend, a+b)
            if len(mod2) >= 1:
                subtrahend = min(subtrahend, mod2[0])

        return total - subtrahend
