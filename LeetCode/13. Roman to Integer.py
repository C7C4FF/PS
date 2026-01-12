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

            
'''
# 두개씩 번갈아가면서 체크. 뒤가 앞보다 크다면 앞을 빼줌...
# IV 는 5에서 1을 빼고, IX 는 10에서 1을 빼는 것과 동일......

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        
        for a, b in zip(s, s[1:]):
            if symbols[a] < symbols[b]:
                ans -= symbols[a]
            else:
                ans += symbols[a]
        
        return ans + symbols[s[-1]]
'''
        

                

