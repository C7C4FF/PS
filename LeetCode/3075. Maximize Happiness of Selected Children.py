# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/

# 최대힙을 만들어도 될듯.. heap = [-x for x in happiness]

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        happiness.sort(reverse=True)

        for i in range(k):
            ans += max(0, happiness[i] - i)
        
        return ans
      
