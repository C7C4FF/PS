# https://leetcode.com/problems/longest-balanced-substring-ii/?envType=daily-question&envId=2026-02-13
# 1가지로만 이루어진 경우, 2가지로 이루어진 경우, 3가지로 이루어진 경우
# 처음 글자가 나온 i 를 외워야 함 > 해시맵으로

class Solution:
    def longestBalanced(self, s: str) -> int:
        def solo(s: str) -> int:
            # 한 글자인 경우를 위해 ans = 1 로 초기화
            cnt = 1
            ans = 1

            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                else:
                    cnt = 1
                ans = max(ans, cnt)

            return ans

        def duo(s: str, ch1: str, ch2: str) -> int:
            diff = 0
            ans = 0
            pos = {0: -1}
            
            for i in range(len(s)):
                if s[i] == ch1:
                    diff += 1
                elif s[i] == ch2:
                    diff -= 1
                else:
                    diff = 0
                    pos = {0: i}
                
                if diff in pos:
                    ans = max(ans, i - pos[diff])
                else:
                    pos[diff] = i

            return ans

        def trio(s: str) -> int:
            ans = 0
            cnt_a, cnt_b, cnt_c = 0, 0, 0
            pos = {(0, 0): -1}

            for i in range(len(s)):
                if s[i] == 'a':
                    cnt_a += 1
                elif s[i] == 'b':
                    cnt_b += 1
                else:
                    cnt_c += 1
                
                distinct = (cnt_a - cnt_b, cnt_b - cnt_c)
                if distinct in pos:
                    ans = max(ans, i - pos[distinct])
                else:
                    pos[distinct] = i
                
            return ans

        ans = max(solo(s),
                duo(s, 'a', 'b'), duo(s, 'a', 'c'), duo(s, 'b', 'c'),
                trio(s))
        return ans
