# https://leetcode.com/problems/sort-vowels-in-a-string/description/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = "AEIOUaeiou"

        temp = []
        
        for i in range(len(s)):
            if s[i] in vowel:
                temp.append(s[i])
                
                s = s[:i] + "." + s[i+1:] 
        
        temp.sort()
        temp = deque(temp)
        
        for i in range(len(s)):
            if s[i] == ".":
                s = s[:i] + temp.popleft() + s[i+1:]


        return s
