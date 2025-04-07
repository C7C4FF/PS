# https://leetcode.com/problems/partition-equal-subset-sum/?envType=daily-question&envId=2025-04-07
# 선택하냐, 선택하지 않느냐 배낭 문제. 0/1 knapsack


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # 총 합이 홀수이면 2로 나눌 수 없음
        if total % 2 != 0:
            return False

        half = total // 2
        
        # dp[j]: j 값을 만들 수 있으면 True
        dp = [True] + [False] * half
        
        for num in nums:
            # 현재 숫자 num으로 가능한 합들을 업데이트
            for j in range(half, num - 1, -1):
                # 이미 가능한 조합이거나, 해당 num으로 만들 수 있는 조합이라면 True로 바꾸기
                dp[j] = dp[j] or dp[j - num]

        return dp[half]
