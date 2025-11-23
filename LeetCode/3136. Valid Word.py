# https://leetcode.com/problems/valid-word/description/
# 길이가 3글자 이상, 숫자 혹은 알파벳만 있음
# 적어도 모음, 자음 하나씩

class Solution:
    def isValid(self, word: str) -> bool:
        vowel = "aeiouAEIOU"
        vowel_chk = False
        consonant_chk = False

        if len(word) < 3:
            return False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch.isalpha():
                if ch not in vowel:
                    consonant_chk = True
                else:
                    vowel_chk = True

        
        if consonant_chk and vowel_chk:
            return True
        else:
            return False
