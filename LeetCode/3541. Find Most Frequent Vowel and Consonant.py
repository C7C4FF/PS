# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = "aeiou"

        vowel_cnt = 0
        conso_cnt = 0
        
        cnt = Counter(s)
        for letter in cnt:
            if letter in vowel:
                vowel_cnt = max(vowel_cnt, cnt[letter])
            else:
                conso_cnt = max(conso_cnt, cnt[letter])

        return vowel_cnt + conso_cnt
