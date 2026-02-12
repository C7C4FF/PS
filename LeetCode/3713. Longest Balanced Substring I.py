# https://leetcode.com/problems/longest-balanced-substring-i/description/?envType=daily-question&envId=2026-02-12
# distinct 글자의 수가 서로 같아야 함 > 밸류를 집합으로 만들었을 때 1개가 나와야 함

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for l in range(n):
            cnt = defaultdict(int)

            for r in range(l, n):
                ch = s[r]
                cnt[ch] += 1
                
                if len(set(cnt.values())) <= 1:
                    ans = max(ans, r-l+1)

        return ans
