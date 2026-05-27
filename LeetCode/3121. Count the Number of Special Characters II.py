# https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/?envType=daily-question&envId=2026-05-27
# 모든 소문자는 대문자가 나오기 전에 나와야 함
# -> 소문자는 매번 갱신해주고, 대문자는 맨 처음 인덱스만 받기

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, upper = [0] * 26, [0] * 26
        lower_idx, upper_idx = [-1] * 26, [-1] * 26

        for i in range(len(word)):
            ch = word[i]

            if ch.isalpha():
                if ch.islower():
                    idx = ord(ch) - ord('a')
                    lower[idx] += 1
                    lower_idx[idx] = i
                else:
                    idx = ord(ch) - ord('A')
                    upper[idx] += 1
                    if upper_idx[idx] == -1:
                        upper_idx[idx] = i
            else:
                continue

        ans = 0
        for i in range(26):
            if lower[i] > 0 and upper[i] > 0:
                if upper_idx[i] > lower_idx[i]:
                    ans += 1

        return ans
