# https://leetcode.com/problems/longest-nice-substring/description/

# 대소문자가 동시에 존재하지 않는 문자는 정답이 될 수 없음 -> 이를 기점으로 나눔
# swapcase() 로 대소문자를 변경할 수 있음 

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        set_s = set(s)

        for i, ch in enumerate(s):
            # 대소문자가 동시에 존재하지 않는 문자가 있다면 이를 기점으로 좌/우로 나눔
            if ch.swapcase() not in set_s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                # 1. 길이가 제일 긴 것 2. 여러개라면 가장 먼저 나온 것을 반환
                # 이를 위해 >= 연산자로 왼쪽에 우선순위를 줌
                return left if len(left) >= len(right) else right

        return s

'''
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i+1, n+1):
                substring = s[i:j]

                if set(substring) == set(substring.swapcase()):
                    if len(substring) > len(ans):
                        ans = substring
        
        return ans
'''
'''
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
'''
