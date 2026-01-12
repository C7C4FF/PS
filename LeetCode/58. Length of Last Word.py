# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
# s.strip() 으로 공백을 한번에 날릴 수도 있음

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        for word in lst[::-1]:
            if word != "":
                return len(word)
            else:
                pass
