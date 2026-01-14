# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        ans = " ".join(words)

        return ans

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        no_ends_space = s.strip()
        lst = no_ends_space.split(' ')
        ans = ""

        for i in range(len(lst)-1, -1, -1):
            if lst[i] == "":
                continue
            
            if i != 0:
                ans += lst[i] + " "
            else:
                ans += lst[i]
        

        return ans
'''
