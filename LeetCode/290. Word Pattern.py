# https://leetcode.com/problems/word-pattern/description/
# 딕셔너리 keyerror 조심하기.. s in s_to_p 아니면 s_to_p.get(s) 로 접근하기

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_lst = list(pattern)
        s_lst = s.split()

        p_to_s = {}
        s_to_p = {}

        if len(s_lst) != len(pattern_lst):
            return False

        for p, s in zip(pattern_lst, s_lst):
            if p in p_to_s and p_to_s[p] != s:
                return False
            if s in s_to_p and s_to_p[s] != p:
                return False

            p_to_s[p] = s
            s_to_p[s] = p

        return True
