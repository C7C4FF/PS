# https://leetcode.com/problems/construct-smallest-number-from-di-string/?envType=daily-question&envId=2025-02-18
# 연속된 D를 세고, 그만큼 수를 스택에 넣음. I가 나오면 스택을 뒤집기

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        temp = []
        counter = 1
        result = ''

        for p in pattern:
            if p == "D":
                # 연속된 D의 개수를 알기 위해서 사용
                counter += 1

            elif counter > 1 and p == "I":
                # D가 이후에 I가 나온 경우
                while counter:
                    temp.append(str(stack.pop(0)))
                    counter -= 1
                
                result += ''.join(temp[::-1])
                temp = []
                counter = 1
            else:
                # I 일때는 가능한 가장 작은 수
                result += str(stack.pop(0))
        
        if counter > 1:
            while counter:
                temp.append(str(stack.pop(0)))
                counter -= 1
        
            result += ''.join(temp[::-1])
        else:
            result += str(stack.pop(0))

        return result
