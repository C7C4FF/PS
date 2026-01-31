# https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=daily-question&envId=2026-01-31
# 파이썬은 ord로 비교할 필요 없이 문자열끼리 비교하면 문자코드로 알아서 비교함

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ch > target:
                return ch

        return letters[0]

'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(1, 122 - ord(target)+1):
            char = chr(ord(target)+i)
            
            try:
                if letters.index(char) >= 0:
                    return char
            except:
                continue

        return letters[0]
'''
