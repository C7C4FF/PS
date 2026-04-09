# https://leetcode.com/problems/maximum-total-reward-using-operations-i/description/
# 작은 값으로 시작해야 큰 값을 계속 더할 수 있음
# dp를 집합으로 처리하기... 

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        ans = {0}
        rewardValues.sort()

        for reward in rewardValues:
            new_rewards = set()
            for x in ans:
                if reward > x:
                    new_rewards.add(x + reward)
            ans.update(new_rewards)
        
        return max(ans)
