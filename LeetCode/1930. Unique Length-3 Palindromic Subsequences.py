# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
# 처음 나온 위치, 마지막으로 나온 위치를 저장
# 그 사이에 있는 글자들의 집합으로 알파벳 개수를 구함

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        ans = 0

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            
            last[idx] = i

        for i in range(26):
            if first[i] == -1: # 등장하지 않았거나
                continue
            elif first[i] == last[i]: # 한글자만 있다면 패스
                continue
            
            start = first[i]
            end = last[i]
            middle = set(s[start+1:end])

            ans += len(middle)

        return ans
