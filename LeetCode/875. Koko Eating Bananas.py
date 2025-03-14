# https://leetcode.com/problems/koko-eating-bananas/
# 이진 탐색으로 먹는 양을 늘리거나 줄여가면서... 

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 10 ** 9
        n = len(piles)

        lo = 1
        hi = max(piles)

        # 주어진 시간 안에 다 처리하려면, 가장 높은 수를 기준으로 먹어야 함
        if h == n:
            return hi
        
        while lo <= hi:
            curr = 0
            mid = (lo + hi) // 2
          
            # 바나나를 먹는 데 걸리는 시간 계산
            # 11을 3으로 나누면 3하고 2가 남는데, 남은 2를 처리하는데도 1시간이 걸리기 때문에 올림 처리
            for banana in piles:
                curr += math.ceil(banana / mid)

            # 주어진 시간보다 빠르거나 같게 먹었다면, 최소를 찾아서 상한선을 줄임
            if curr <= h:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
