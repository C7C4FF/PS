# https://leetcode.com/problems/maximum-gap/description/
# 정렬하는 순간 linear time, linear extra space 제약 조건에 맞지 않음
# 최대값과 최소값 사이를 n-1 개로 균등하게 나눈다고 가정
# 각 버킷마다 최소값, 최댓값을 저장. 현재 버킷의 최솟값 - 이전 버킷의 최댓값 중 가장 큰 걸 찾기

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0
        
        high, low = max(nums), min(nums)
        if high == low:
            return 0

        gap = max(1, (high - low) // (n - 1))
        buckets = [[float('inf'), float('-inf')] for _ in range((high - low) // gap + 1)]

        for num in nums:
            idx = (num - low) // gap
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        ans = 0
        prev_max = low
        for bucket in buckets:
            if bucket[0] != float('inf'):
                ans = max(ans, bucket[0] - prev_max)
                prev_max = bucket[1]

        return ans
