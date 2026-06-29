# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/?envType=daily-question&envId=2026-06-29

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0

        for i in range(len(patterns)):
            if patterns[i] in word:
                ans += 1

        return ans
