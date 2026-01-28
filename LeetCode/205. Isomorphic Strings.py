# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150
# 각 위치에서의 대응관계를 확인하기

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for ch_s, ch_t in zip(s, t):
            # 이미 s의 글자가 매핑된 적이 있으면 값이 같아야 함
            if ch_s in s_to_t:
                if s_to_t[ch_s] != ch_t:
                    return False
            else:
                s_to_t[ch_s] = ch_t

            # t가 매핑된 적이 있으면 값 확인
            if ch_t in t_to_s:
                if t_to_s[ch_t] != ch_s:
                    return False
            else:
                t_to_s[ch_t] = ch_s

        return True

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cnt_s = Counter(s).most_common()
        cnt_t = Counter(t).most_common()

        substitution = defaultdict()
        ans = ""

        for i in range(len(cnt_s)):
            k = cnt_s[i][0] if i < len(cnt_s) else None
            v = cnt_t[i][0] if i < len(cnt_t) else None

            if k is None:
                continue

            substitution[k] = v
        
        for ch in s:
            try:
                ans += substitution[ch]
            except:
                return False

        return True if t == ans else False
'''
