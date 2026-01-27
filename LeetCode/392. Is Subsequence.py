# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = list(s)

        for ch in t:
            if len(q) == 0:
                return True
            if ch == q[0]:
                q.pop(0)
        
        if len(q) == 0:
            return True
        else:
            return False

        
        
