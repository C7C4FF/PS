# https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1 # 1이면 양수, -1이면 음수
        num = 0
        total = 0

        for ch in s:
            if ch.isdigit():
                # 연속된 정수를 하나로 만들기
                num = num * 10 + int(ch)

            elif ch == '+':
                total += sign * num
                sign, num = 1, 0
            elif ch == '-':
                total += sign * num
                sign, num = -1, 0

            elif ch == '(':
                stack.append([sign, total])
                total = 0
                sign = 1
            elif ch == ')':
                total += sign * num
                num = 0
                prev_sign, prev_total = stack.pop()
                total = (prev_sign * total) + prev_total
        
        return total + sign * num
