# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150
# 뒤에서부터 앞으로 가며 체크

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        specials = {"IV": 4 , "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        ans = 0
        temp = ""
        
        for i in reversed(range(len(s))):
            ch = s[i]
            temp = ch + temp

            if temp in specials:
                ans -= symbols[s[i+1]]
                ans += specials[temp]
            else:
                ans += symbols[ch]

            if len(temp) >= 2:
                temp = temp[:-1]

        return ans

            

        

                

