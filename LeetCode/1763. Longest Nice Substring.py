# https://leetcode.com/problems/longest-nice-substring/description/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = defaultdict(list)
        n = len(s)
        
        size = 1
        seen = [s]

        while size < n:
            for i in range(0, n-size+1):
                seen.append(s[i:i+size])
            size += 1
        
        for substring in seen:
            cnt = Counter(substring)
            
            flag = False
            for ch in substring:
                if cnt[ch.upper()] and cnt[ch.lower()]:
                    flag = True
                else:
                    flag = False
                    break
            
            if flag:
                ans[len(substring)].append(substring)

        for i in range(n, 0, -1):
            if ans[i]:
                return ans[i][0]

        return ""
