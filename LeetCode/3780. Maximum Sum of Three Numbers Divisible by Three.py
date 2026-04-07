# 1. 나머지가 다른 숫자들 1개씩 뽑기 2. 같은 나머지를 가진 것들 3개 뽑기
# 최대힙으로 넣기. > 1개씩 이상 있다면, 최댓값만 뽑아서 더하기
# 3개 이상 있다면, 최댓값을 3번 뽑아서 계산하기

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        remain = {0: [], 1: [], 2: []}

        for num in nums:
            r = num % 3
            heapq.heappush(remain[r], -num)

        if remain[0] and remain[1] and remain[2]:
            ans = min(ans, remain[0][0] + remain[1][0] + remain[2][0])
        
        for i in range(3):
            if len(remain[i]) >= 3:
                sum_remain = 0
                for _ in range(3):
                    sum_remain += heapq.heappop(remain[i])
                ans = min(ans, sum_remain)
        
        return -ans
