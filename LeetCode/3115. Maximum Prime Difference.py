# https://leetcode.com/problems/maximum-prime-difference/description/
# 소수라면 힙에 넣고 최소값, 최댓값 구해주기
# 거리가 가장 멀기 위해서는 가장 왼쪽에 있던 소수와 가장 오른쪽에 있는 소수의 거리를 구해야함

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2: return False

            d = 2
            while d * d <= n:
                if n % d == 0:
                    return False
                else:
                    d += 1
            
            return True

        n = len(nums)
        prime_lst = []

        for i in range(n):
            n = nums[i]
            if is_prime(n):
                heapq.heappush(prime_lst, i)

        return prime_lst[-1] - prime_lst[0]
