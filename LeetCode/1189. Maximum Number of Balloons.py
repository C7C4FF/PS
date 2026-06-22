# https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-22
# {'a': 1, 'b': 1, 'l': 2, 'o': 2, 'n': 1}

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        cnt = Counter(text)

        ans = min(cnt['a'], cnt['b'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])
        
        return ans
            
        
