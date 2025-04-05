# https://leetcode.com/problems/daily-temperatures/

# 단순 이중 반복문 투포인터로는 TLE
# 모노토닉 스택?

# i) 스택이 빈 경우 -> 스택에 넣어주기
# ii) 스택이 있는 경우 -> 현재 온도와 스택 top의 온도를 비교하고, 현재가 더 크다면 스택에서 pop. 현재 인덱스와의 차를 넣어줌

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * n
        stack = []
      
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)
            
        return ans

'''
# TLE 35 / 48

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            today = temperatures[i]
            for j in range(i+1, n):
                ans[i] += 1
                if temperatures[j] > today:
                    break
            else:
                ans[i] = 0
        
        return ans
'''
