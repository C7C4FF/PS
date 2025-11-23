# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        txt = text.split(" ")
        cnt = 0
        for word in txt:
            flag = True
            for letter in word:
                if letter in brokenLetters:
                    flag = False
                    break
            
            if flag:
                cnt += 1
        
        return cnt
