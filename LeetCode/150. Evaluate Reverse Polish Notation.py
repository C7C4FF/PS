# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Reverse Polish Notation > Postfix Notation 후위 표기법
# truncates toward zero > int() 로 구현
# eval() 은 들어온 것 그대로 계산해줌. 나눗셈을 위해 num1, num2의 순서 바꿔주기

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for ch in tokens:
            if len(ch) == 1:
                if ch.isnumeric():
                    numbers.append(ch)
                else:
                    num1, num2 = numbers.pop(), numbers.pop()
                    num = int(eval(f'{num2}{ch}{num1}'))
                    numbers.append(num)
            else:
                numbers.append(int(ch))
            
        return numbers[0]

            

        
