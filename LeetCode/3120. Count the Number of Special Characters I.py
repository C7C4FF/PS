# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=daily-question&envId=2026-05-26
# 리스트를 하나로 쓰기에는 'Z' 가 끝난 이후 아스키 코드가 [, ] 등으로 바로 이어지지 않음.
# -> 소문자와 대문자를 따로따로 구분

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, upper = [0] * 26, [0] * 26

        for ch in word:
            if ch.isalpha():
                if ch.islower():
                    lower[ord(ch) - ord('a')] += 1
                else:
                    upper[ord(ch) - ord('A')] += 1
            else:
                continue

        return sum(1 for l, u in zip(lower, upper) if l > 0 and u > 0)
