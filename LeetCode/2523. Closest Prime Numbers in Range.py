# https://leetcode.com/problems/closest-prime-numbers-in-range/?envType=daily-question&envId=2025-03-07
# 에라토스테네스의 체 -> 힙으로 최소값 찾기.


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = []
        primes = []
        nums = [False, False] + [True] * (right - 1)
        for i in range(2, right+1):
            if nums[i] == True:
                primes.append(i)
                for j in range(i*2, right+1, i):
                    nums[j] = False
        
        primes = list(filter(lambda x : left <= x <= right, primes))
        
        if len(primes) < 2:
            return [-1, -1]
        else:
            for i in range(len(primes)-1):
                l, r = primes[i], primes[i+1]
                gap = r - l
                heapq.heappush(ans, (gap, [l, r]))
            return ans[0][1]
