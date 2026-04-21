# https://leetcode.com/problems/apply-operations-to-make-string-empty/description/

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)

        most_freq = max(cnt.values())
        most_freq_items = [k for k, v in cnt.items() if v == most_freq]

        lst = []
        for ch in most_freq_items:
            idx = s.rfind(ch)
            lst.append((idx, ch))

        lst.sort()
        ans = ""
        for idx, ch in lst:
            ans += ch

        return ans
